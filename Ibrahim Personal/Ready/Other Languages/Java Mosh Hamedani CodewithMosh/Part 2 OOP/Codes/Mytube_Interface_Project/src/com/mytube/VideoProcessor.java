package com.mytube;

import java.security.Provider;

public class VideoProcessor {
    private XVideoEncoder encoder;
    private XVideoDatabase database;
    private XEmailService emailService;

    public VideoProcessor (VideoEncoder encoder, VideoDatabase  database, EmailService emailService) {
        this.encoder = encoder;
        this.database = database;
        this.emailService = emailService;
    }

    public void process(Video video) {

        //var encoder = new VideoEncoder();
        encoder.encode(video);

        //var database = new VideoDatabase();
        database.store(video);

        //var emailService = new EmailService();
        emailService.sendEmail(video.getUser());
    }

    public void setEncoder (VideoEncoder encoder) {
        this.encoder = encoder;
    }

}

