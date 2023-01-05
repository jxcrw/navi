package com.goinggolfpro.goinggolfpro3;

import java.util.ArrayList;
import java.util.Date;

/**
 * Created by Jak on 2014/09/21.
 */
public class GolfSkill {
    private String mName;
    private Date mStartTime;
    private Date mEndTime;
    private int mBallsHit;
    private float mDuration; //in hours
    private ArrayList<GolfClub> mGolfClubs;

    public GolfSkill(String name) {
        mName = name;
        mStartTime = new Date();
        mBallsHit = 0;
        mDuration = 0;
        mGolfClubs = new ArrayList<GolfClub>();
        mEndTime = null;
    }

    public String getName() {
        return mName;
    }

    public void setName(String name) {
        mName = name;
    }

    public Date getStartTime() {
        return mStartTime;
    }

    public void setStartTime(Date startTime) {
        mStartTime = startTime;
    }

    public Date getEndTime() {
        return mEndTime;
    }

    public void setEndTime(Date endTime) {
        mEndTime = endTime;
    }

    public int getBallsHit() {
        int ballsHit = 0;
        for (GolfClub golfClub : mGolfClubs) {
            ballsHit += golfClub.getBallsHit();
        }
        mBallsHit = ballsHit;
        return mBallsHit;
    }

    public void setBallsHit(int ballsHit) {
        mBallsHit = ballsHit;
    }

    public float getDuration() {
        float durationInMillis = mEndTime.getTime() - mStartTime.getTime();
        mDuration = durationInMillis/3600000;
        return mDuration;
    }

    public void setDuration(float duration) {
        mDuration = duration;
    }

    public ArrayList<GolfClub> getGolfClubs() {
        return mGolfClubs;
    }

    public void setGolfClubs(ArrayList<GolfClub> golfClubs) {
        mGolfClubs = golfClubs;
    }


}
