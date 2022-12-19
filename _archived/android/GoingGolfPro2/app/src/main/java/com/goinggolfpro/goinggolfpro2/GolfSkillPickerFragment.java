package com.goinggolfpro.goinggolfpro2;

import android.app.AlertDialog;
import android.app.Dialog;
import android.app.DialogFragment;
import android.os.Bundle;

/**
 * Created by Jak on 2014/09/07.
 */
public class GolfSkillPickerFragment extends DialogFragment {

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        builder.setTitle(R.string.golf_skill_picker_title)
               .setItems(R.array.skill_list, null)
               .setNegativeButton(android.R.string.cancel, null);

        return builder.create();
    }
}
