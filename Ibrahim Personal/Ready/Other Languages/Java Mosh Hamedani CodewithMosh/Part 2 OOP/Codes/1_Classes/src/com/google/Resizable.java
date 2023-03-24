package com.google;

public interface Resizable {
    void resize();
    void resize(int size);
    void resize(int x, int y);
    void resizeTo(UIWidget widget);

}
