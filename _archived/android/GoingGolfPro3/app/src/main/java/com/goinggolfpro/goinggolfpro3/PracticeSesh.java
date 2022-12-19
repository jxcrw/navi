package com.goinggolfpro.goinggolfpro3;

import java.util.ArrayList;
import java.util.Date;
import java.util.UUID;

/**
 * Created by Jak on 2014/09/21.
 */
public class PracticeSesh {
    private UUID mId;
    private Date mDate;
    private String mVenue;
    private ArrayList<GolfSkill> mGolfSkills;
    private int mTotalBallsHit;
    private float mTotalDuration; //in hours

    public PracticeSesh() {
        mId = UUID.randomUUID();
        mDate = new Date();
        mGolfSkills = new ArrayList<GolfSkill>();
        mTotalBallsHit = 0;
        mTotalDuration = 0;
    }

    public UUID getId() {
        return mId;
    }

    public Date getDate() {
        return mDate;
    }

    public void setDate(Date date) {
        mDate = date;
    }

    public String getVenue() {
        return mVenue;
    }

    public void setVenue(String venue) {
        mVenue = venue;
    }

    public ArrayList<GolfSkill> getGolfSkills() {
        return mGolfSkills;
    }

    public void setGolfSkills(ArrayList<GolfSkill> golfSkills) {
        mGolfSkills = golfSkills;
    }

    public int getTotalBallsHit() {
        int totalBallsHit = 0;
        for (GolfSkill golfSkill : mGolfSkills) {
            totalBallsHit += golfSkill.getBallsHit();
        }
        mTotalBallsHit = totalBallsHit;
        return mTotalBallsHit;
    }

    public void setTotalBallsHit(int totalBallsHit) {
        mTotalBallsHit = totalBallsHit;
    }

    public float getTotalDuration() {
        float totalDuration = 0;
        for (GolfSkill golfSkill : mGolfSkills) {
            totalDuration += golfSkill.getDuration();
        }
        mTotalDuration = totalDuration;
        return mTotalDuration;
    }

    public void setTotalDuration(float totalDuration) {
        mTotalDuration = totalDuration;
    }


}
