package com.mytube;

public class Main {

    public static void main(String[] args) {
        var encoder = new VideoEncoder();
        var database = new VideoDatabase();
        var emailService = new EmailService();

        //var videoprocessor = new VideoProcessor(encoder, database, emailService);

        var video = new Video();
        video.setFileName("birthday.mp4");
        video.setTitle("Jennifer's birthday");
        video.setUser(new User("john@domain.com"));

        var processor = new VideoProcessor(encoder, database, emailService);
        processor.setEncoder(encoder);
        processor.process(video);
    }
}
