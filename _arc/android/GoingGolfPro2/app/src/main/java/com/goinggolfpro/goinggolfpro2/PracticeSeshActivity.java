package com.goinggolfpro.goinggolfpro2;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.FragmentManager;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;


public class PracticeSeshActivity extends Activity {

    private static final String DIALOG_SKILL_PICKER = "skill_picker";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_practice_sesh);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.practice_sesh, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        switch (item.getItemId()) {
            case R.id.action_new:
                //Open a dialog with the various golf skills
                FragmentManager fm = this.getFragmentManager();
                GolfSkillPickerFragment skill_picker = new GolfSkillPickerFragment();
                skill_picker.show(fm, DIALOG_SKILL_PICKER);
                return true;

            default:
                return super.onOptionsItemSelected(item);
        }
    }
}
