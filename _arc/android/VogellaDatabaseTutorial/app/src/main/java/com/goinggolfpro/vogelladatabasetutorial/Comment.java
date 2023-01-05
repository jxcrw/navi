package com.goinggolfpro.vogelladatabasetutorial;

/**
 * Created by Jak on 2014/09/14.
 */
public class Comment {
    private long mId;
    private String mComment;

    public long getId() {
        return mId;
    }

    public void setId(long id) {
        mId = id;
    }

    public String getComment() {
        return mComment;
    }

    public void setComment(String comment) {
        mComment = comment;
    }

    // Will be used by the ArrayAdapter in the ListView
    @Override
    public String toString() {
        return mComment;
    }
}
