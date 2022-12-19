package com.goinggolfpro.criminalintent;

import android.app.Fragment;

/**
 * Created by Jak on 2014/11/05.
 */
public class CrimeListActivity extends SingleFragmentActivity {

    @Override
    protected Fragment createFragment() {
        return new CrimeListFragment();
    }
}
