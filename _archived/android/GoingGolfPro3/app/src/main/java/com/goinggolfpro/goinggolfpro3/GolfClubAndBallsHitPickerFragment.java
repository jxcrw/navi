package com.goinggolfpro.goinggolfpro3;

import android.app.AlertDialog;
import android.app.Dialog;
import android.app.DialogFragment;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.NumberPicker;

/**
 * Created by Jak on 2014/09/27.
 */
public class GolfClubAndBallsHitPickerFragment extends DialogFragment {
    public static final String EXTRA_ITEM_POSITION =
            "com.goinggolfpro.goinggolfpro.golf_skill";
    public static final String EXTRA_GOLF_SKILL =
            "com.goinggolfpro.goinggolfpro.golf_skill";
    private NumberPicker mGolfClubPicker;
    private NumberPicker mBallsHitPicker;
    private String[] mGolfClubList;

    private void sendResult(int resultCode) {
        if (getTargetFragment() == null)
            return;

        Intent i = new Intent();
        i.putExtra(EXTRA_ITEM_POSITION, resultCode);

        getTargetFragment()
                .onActivityResult(getTargetRequestCode(), resultCode, i);
    }

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        View view = getActivity().getLayoutInflater().inflate(R.layout.fragment_golfclubandballshitpicker, null);

        mGolfClubPicker = (NumberPicker)view.findViewById(R.id.golf_club_picker);
        mGolfClubList = getResources().getStringArray(R.array.golf_club_list);
        mGolfClubPicker.setMinValue(0);
        mGolfClubPicker.setMaxValue(mGolfClubList.length - 1);
        mGolfClubPicker.setDisplayedValues(mGolfClubList);
        mGolfClubPicker.setWrapSelectorWheel(true);

//        mBallsHitPicker= (NumberPicker)view.findViewById(R.id.balls_hit_picker);
//        mBallsHitPicker.setMinValue(0);
//        mBallsHitPicker.setMaxValue(1000);
//        mBallsHitPicker.setWrapSelectorWheel(false);

        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        builder.setTitle(R.string.golf_club_and_balls_hit_picker_title)
                .setView(view)
                .setPositiveButton(android.R.string.ok, null)
                .setNegativeButton(android.R.string.cancel, null);

        return builder.create();
    }
}
