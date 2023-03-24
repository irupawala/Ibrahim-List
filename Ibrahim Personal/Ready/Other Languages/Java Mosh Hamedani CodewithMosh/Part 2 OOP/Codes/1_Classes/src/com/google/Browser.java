package com.google;

public class Browser {
    public void navigate (String address) {
        String ip = findIPAddress(address);
        String html = sendHTTPrequest(ip);
        System.out.println(html);
    }

    private String sendHTTPrequest(String ip) {
        return "<html><html>";
    }

    private String findIPAddress(String address) {
        return "10.195.64.87";
    }
}
