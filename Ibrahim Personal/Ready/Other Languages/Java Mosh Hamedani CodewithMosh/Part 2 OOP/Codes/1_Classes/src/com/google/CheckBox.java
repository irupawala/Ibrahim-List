package com.google;

public final class CheckBox extends UIControl {
//public abstract class CheckBox extends UIControl { // If method is not overridden then class should be declared as abstract

    @Override
    public void render() {
        System.out.println("Render CheckBox");
    }



}




// public class MyCheckBox extends CheckBox {} Cannot inherit from final class
