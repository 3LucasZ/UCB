function w = euler(f, a, b, h, w1, ax1)
    w = w1;
    for t=a+h:h:b
        w = w+f(t,w)*h;
        disp([t, w]);
        plot(ax1, t, w, ".", 'MarkerSize', 10);
    end
end