package com.google;

public abstract class UIControl {
    protected boolean isEnabled = true;


    public UIControl() {
        System.out.println("UI Control");
    }

    public UIControl(boolean isEnabled) {
        this.isEnabled = isEnabled;
        System.out.println("UI Parameterized Control");
    }

    public abstract void render();

    public final void enable() {
        isEnabled = true;
    }

    public void disable() {
        isEnabled = false;
    }

    public boolean isEnabled() {
        return isEnabled;
    }
}
