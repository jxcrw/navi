package com.goinggolfpro.goinggolfpro3;

/**
 * Created by Jak on 2014/09/22.
 */
public class GolfClub {
    private String mName;
    private int mBallsHit;
    private int mDistance;

    public GolfClub(String clubName) {
        mName = clubName;
    }

    public String getName() {
        return mName;
    }

    public void setName(String name) {
        mName = name;
    }

    public int getBallsHit() {
        return mBallsHit;
    }

    public void setBallsHit(int ballsHit) {
        mBallsHit = ballsHit;
    }

    public int getDistance() {
        return mDistance;
    }

    public void setDistance(int distance) {
        mDistance = distance;
    }
}
