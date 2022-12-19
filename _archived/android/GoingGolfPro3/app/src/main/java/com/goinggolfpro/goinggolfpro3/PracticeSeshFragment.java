package com.goinggolfpro.goinggolfpro3;


import android.app.ActionBar;
import android.app.Fragment;
import android.app.FragmentManager;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ExpandableListView;
import android.widget.TextView;

import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Random;


/**
 * A simple {@link Fragment} subclass.
 *
 */
public class PracticeSeshFragment extends Fragment {
    private static final String DEBUG_TAG = "DebugTag";
    private static final String DIALOG_SKILL_PICKER = "skill_picker_dialog";
    private static final int DIALOG_SKILL_PICKER_CODE = 0;
    private static final String DIALOG_CLUBANDBALL_PICKER = "clubandball_picker_dialog";
    private static final int DIALOG_CLUBANDBALL_PICKER_CODE = 1;
    public PracticeSesh mPracticeSesh;
    private ExpandableListView mExpandableGolfSkillListView;
    private ExpandableGolfSkillListAdapter mExpandableGolfSkillListAdapter;
    private TextView mPracticeSeshDateTextView;
    private TextView mPracticeSeshTotalBallsHitTextView;
    private TextView mPracticeSeshDurationTextView;
    private Button mDebugButton;

    public PracticeSeshFragment() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mPracticeSesh = new PracticeSesh();
        setHasOptionsMenu(true);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_practicesesh, container, false);

        ActionBar actionBar = getActivity().getActionBar();
        actionBar.setTitle("New Practice Session");

        mPracticeSeshDateTextView = (TextView)view.findViewById(R.id.practicesesh_date);
        mPracticeSeshDateTextView.setText(new SimpleDateFormat("EEEE M/d/yyyy").format(mPracticeSesh.getDate()));

        mPracticeSeshTotalBallsHitTextView = (TextView)view.findViewById(R.id.practicesesh_balls_hit);
        mPracticeSeshDurationTextView = (TextView)view.findViewById(R.id.practicesesh_duration);

        mExpandableGolfSkillListView = (ExpandableListView)view.findViewById(R.id.expandableListView);
//        mPracticeSesh = createDummyPracticeSesh();
        mExpandableGolfSkillListAdapter = new ExpandableGolfSkillListAdapter(getActivity(),
                                                                             mPracticeSesh,
                                                                             mExpandableGolfSkillListView,
                                                                             mPracticeSeshTotalBallsHitTextView,
                                                                             mPracticeSeshDurationTextView);
        mExpandableGolfSkillListView.setAdapter(mExpandableGolfSkillListAdapter);
        mExpandableGolfSkillListView.setOnChildClickListener(new ExpandableListView.OnChildClickListener() {
            @Override
            public boolean onChildClick(ExpandableListView expandableListView, View view, int groupPosition, int childPosition, long id) {
                Log.d(DEBUG_TAG, "Click");
                FragmentManager fm = getFragmentManager();
                GolfClubAndBallsHitPickerFragment dialog = new GolfClubAndBallsHitPickerFragment();
                dialog.setTargetFragment(PracticeSeshFragment.this, DIALOG_CLUBANDBALL_PICKER_CODE);
                dialog.show(fm, DIALOG_CLUBANDBALL_PICKER);
                return false;
            }
        });

        mDebugButton = (Button)view.findViewById(R.id.debug_button);
        mDebugButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.d(DEBUG_TAG, "Total balls hit = " + String.valueOf(mPracticeSesh.getTotalBallsHit()));
                Log.d(DEBUG_TAG, "Practicesesh duration = " + String.valueOf(new DecimalFormat("#.#######").format(mPracticeSesh.getTotalDuration())) + " hrs");
                int i = 0;
                for (GolfSkill golfSkill : mPracticeSesh.getGolfSkills()) {
                    Log.d(DEBUG_TAG, "Golfskill #" + String.valueOf(i) + " = " + golfSkill.getName());
                    i++;
                }
            }
        });

        return view;
    }

    public void updateActionBar() {
        ActionBar actionBar = getActivity().getActionBar();
        actionBar.setTitle("New Practice Session");
//        actionBar.setTitle(new SimpleDateFormat("EEEE M/d/yyyy").format(mPracticeSesh.getDate()));
//        actionBar.setSubtitle(String.valueOf(new DecimalFormat("#.##").format(mPracticeSesh.getTotalDuration())) + " hrs, "  +
//                String.valueOf(mPracticeSesh.getTotalBallsHit()) + " balls");
    }

    public void createGolfSkill(String golfSkillName) {
        GolfSkill golfSkill = new GolfSkill(golfSkillName);
//        golfSkill.setEndTime(new Date(golfSkill.getStartTime().getTime() + (new Random().nextInt(90 - 15) + 15) * 60000));
        mPracticeSesh.getGolfSkills().add(golfSkill);
        mExpandableGolfSkillListAdapter.notifyDataSetChanged();
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == DIALOG_SKILL_PICKER_CODE) {
            int itemPosition = data.getIntExtra(GolfSkillPickerFragment.EXTRA_ITEM_POSITION, 0);
            switch (itemPosition) {
                case 0:
                    createGolfSkill("Putt");
                    Log.d(DEBUG_TAG, "Total balls hit = " + String.valueOf(mPracticeSesh.getTotalBallsHit()));
                    return;
                case 1:
                    createGolfSkill("Chip/Pitch");
                    Log.d(DEBUG_TAG, "Total balls hit = " + String.valueOf(mPracticeSesh.getTotalBallsHit()));
                    return;
                case 2:
                    createGolfSkill("Bunker");
                    Log.d(DEBUG_TAG, "Total balls hit = " + String.valueOf(mPracticeSesh.getTotalBallsHit()));
                    return;
                case 3:
                    createGolfSkill("Tee/Approach");
                    Log.d(DEBUG_TAG, "Total balls hit = " + String.valueOf(mPracticeSesh.getTotalBallsHit()));
                    return;
            }
        }
    }

    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        // Inflate the menu; this adds items to the action bar if it is present.
        inflater.inflate(R.menu.practice_sesh, menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        switch (item.getItemId()) {
            case R.id.action_new:
                //Open a dialog with the various golf skills
                FragmentManager fm = getFragmentManager();
                GolfSkillPickerFragment dialog = new GolfSkillPickerFragment();
                dialog.setTargetFragment(PracticeSeshFragment.this, DIALOG_SKILL_PICKER_CODE);
                dialog.show(fm, DIALOG_SKILL_PICKER);
                return true;

            default:
                return super.onOptionsItemSelected(item);
        }
    }

    public PracticeSesh createDummyPracticeSesh() {

        PracticeSesh practiceSesh = new PracticeSesh();

        String[] golfskill_names = {"Putt", "Chip/Pitch", "Bunker", "Tee/Approach"};
        String[] golfclub_names = {"Putter", "9 iron", "56°", "Driver"};

        ArrayList<GolfSkill> golfSkills = new ArrayList<GolfSkill>();
        for (String golfskill_name : golfskill_names) {
            GolfSkill golfSkill = new GolfSkill(golfskill_name);

            ArrayList<GolfClub> golfClubs = new ArrayList<GolfClub>();
            for(String golfclub_name : golfclub_names) {
                GolfClub golfClub = new GolfClub(golfclub_name);
                golfClub.setBallsHit(new Random().nextInt((50 - 1) + 1));
                golfClubs.add(golfClub);
            }

            golfSkill.setGolfClubs(golfClubs);
            golfSkills.add(golfSkill);
        }
        practiceSesh.setGolfSkills(golfSkills);
        return practiceSesh;
    }
}


