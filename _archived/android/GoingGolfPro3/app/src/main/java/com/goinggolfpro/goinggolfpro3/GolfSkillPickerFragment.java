package com.goinggolfpro.goinggolfpro3;

import android.app.AlertDialog;
import android.app.Dialog;
import android.app.DialogFragment;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

/**
 * Created by Jak on 2014/09/27.
 */
public class GolfSkillPickerFragment extends DialogFragment {
    public static final String EXTRA_ITEM_POSITION =
            "com.goinggolfpro.goinggolfpro.golf_skill";
    public static final String EXTRA_GOLF_SKILL =
            "com.goinggolfpro.goinggolfpro.golf_skill";

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
        View view = getActivity().getLayoutInflater().inflate(R.layout.fragment_golfskill_picker, null);

        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        builder.setTitle(R.string.golf_skill_picker_title)
                .setItems(R.array.skill_list, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int itemPosition) {
                        sendResult(itemPosition);
                    }
                });

        return builder.create();
    }
}
