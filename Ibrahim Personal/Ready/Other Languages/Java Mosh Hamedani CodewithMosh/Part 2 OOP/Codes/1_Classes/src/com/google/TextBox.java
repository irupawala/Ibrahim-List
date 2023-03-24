package com.google;

public class TextBox extends UIControl{
    private String text = ""; // Field

    public TextBox() {
        System.out.println("Text Box");
    }

    @Override
    public String toString() {
        return text;
    }

    @Override
    public void render() {
        System.out.println("Render TextBox");
    }

    public void setText(String text) {
        this.text = text;
    }

    public void clear() {
        text = "";
    }

}
