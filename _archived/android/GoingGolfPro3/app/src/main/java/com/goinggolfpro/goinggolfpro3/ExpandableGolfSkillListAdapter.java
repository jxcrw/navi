package com.goinggolfpro.goinggolfpro3;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseExpandableListAdapter;
import android.widget.ExpandableListView;
import android.widget.ImageButton;
import android.widget.TextView;

import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

/**
 * Created by Jak on 2014/09/22.
 */
public class ExpandableGolfSkillListAdapter extends BaseExpandableListAdapter {
    private static final String TAG = "ExpandableGolfSkillListAdapter";
    private static final String DEBUG_TAG = "DebugTag";
    private Context mContext;
    private ArrayList<GolfSkill> mGolfSkills;
    private PracticeSesh mPracticeSesh;
    private ExpandableListView mExpandableListView;
    private TextView mBallsHitTextView;
    private TextView mEndTimeTextView;
    private ImageButton mAddClubButton;
    private ImageButton mStopGolfSkillButton;
    private TextView mPracticeSeshTotalBallsHitTextView;
    private TextView mPracticeSeshDurationTextView;

    // Trying to add a new dialog.


    public ExpandableGolfSkillListAdapter(Context context, PracticeSesh practiceSesh,
                                          ExpandableListView expandableListView, TextView practiceSeshTotalBallsHitTextView,
                                          TextView practiceSeshDurationTextView) {
        this.mContext = context;
        this.mPracticeSesh = practiceSesh;
        this.mGolfSkills = practiceSesh.getGolfSkills();
        this.mExpandableListView = expandableListView;
        this.mPracticeSeshTotalBallsHitTextView = practiceSeshTotalBallsHitTextView;
        this.mPracticeSeshDurationTextView = practiceSeshDurationTextView;
    }

    @Override
    public Object getChild(int groupPosition, int childPosition) {
        ArrayList<GolfClub> golfClubList = mGolfSkills.get(groupPosition).getGolfClubs();
        return golfClubList.get(childPosition);
    }

    @Override
    public View getGroupView(final int groupPosition, boolean isExpanded,
                             View convertView, final ViewGroup parent) {
        final GolfSkill golfSkill = (GolfSkill)getGroup(groupPosition);
        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater) mContext
                    .getSystemService(mContext.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.fragment_golfskill_grouprow, parent, false);
        }

        TextView golfSkillNameTextView = (TextView)convertView.findViewById(R.id.golfskill_name);
        golfSkillNameTextView.setText(golfSkill.getName());

        final SimpleDateFormat simpleDateFormat = new SimpleDateFormat("HH:mm");
        String startTime = simpleDateFormat.format(golfSkill.getStartTime());
        TextView golfSkillStartTimeTextView = (TextView)convertView.findViewById(R.id.golfskill_start_time);
        golfSkillStartTimeTextView.setText(startTime);

        mBallsHitTextView = (TextView)convertView.findViewById(R.id.golfskill_balls_hit);
        mEndTimeTextView = (TextView)convertView.findViewById(R.id.golfskill_end_time);

        mAddClubButton = (ImageButton)convertView.findViewById(R.id.add_club_button);
        mAddClubButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                GolfClub golfClub = new GolfClub("Driver");
                golfClub.setBallsHit(20);
                golfSkill.getGolfClubs().add(golfClub);

                mBallsHitTextView.setText(String.valueOf(golfSkill.getBallsHit()));
                notifyDataSetChanged();
                mExpandableListView.expandGroup(groupPosition, true);
            }
        });

        mStopGolfSkillButton = (ImageButton)convertView.findViewById(R.id.stop_skill_button);
        mStopGolfSkillButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                golfSkill.setEndTime(new Date());
                golfSkill.setEndTime(new Date(golfSkill.getStartTime().getTime() + (627) * 60000));
                String endTime = simpleDateFormat.format(golfSkill.getEndTime());
                mEndTimeTextView.setText(endTime);
                mAddClubButton.setEnabled(false);
                mStopGolfSkillButton.setEnabled(false);
                mPracticeSeshTotalBallsHitTextView.setText(String.valueOf(mPracticeSesh.getTotalBallsHit()) + " balls");
                mPracticeSeshDurationTextView.setText((String.valueOf(new DecimalFormat("#.#").format(mPracticeSesh.getTotalDuration())) + " hours "));
                notifyDataSetChanged();
                mExpandableListView.collapseGroup(groupPosition);
            }
        });

        return convertView;
    }

    @Override
    public long getChildId(int groupPosition, int childPosition) {
        return childPosition;
    }

    @Override
    public View getChildView(int groupPosition, int childPosition,
                             boolean isLastChild, View convertView, ViewGroup parent) {
        GolfClub golfClub = (GolfClub)getChild(groupPosition, childPosition);
        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater)mContext
                    .getSystemService(mContext.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.fragment_golfskill_childrow, parent, false);
        }

        TextView clubTextView = (TextView)convertView.findViewById(R.id.club_name);
        clubTextView.setText(golfClub.getName().toString());
        TextView ballsTextView = (TextView)convertView.findViewById(R.id.golfclub_balls_hit);
        ballsTextView.setText(Integer.toString(golfClub.getBallsHit()) + " balls");

        return convertView;
    }

    @Override
    public int getChildrenCount(int groupPosition) {
        ArrayList<GolfClub> golfClubList = mGolfSkills.get(groupPosition).getGolfClubs();
        return golfClubList.size();
    }

    @Override
    public Object getGroup(int groupPosition) {
        return mGolfSkills.get(groupPosition);
    }

    @Override
    public int getGroupCount() {
        return mGolfSkills.size();
    }

    @Override
    public long getGroupId(int groupPosition) {
        return groupPosition;
    }

    @Override
    public boolean hasStableIds() {
        return true;
    }

    @Override
    public boolean isChildSelectable(int groupPosition, int childPosition) {
        return true;
    }
}
