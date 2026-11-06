/* Strichfigur-Helfer: feste Keyframes, kein Zufall. Lädt nach gsap.min.js. */
(function () {
  var LIMBS = ["thL", "thR", "shL", "shR", "uaL", "uaR", "faL", "faR"];

  function sel(p, names) {
    return names.map(function (n) { return "#" + p + "-" + n; }).join(",");
  }

  window.Fig = {
    /* Gelenke drehen um ihren Ursprung (Hüfte bzw. Schulter bzw. Knie/Ellbogen). */
    init: function (p) {
      gsap.set(sel(p, LIMBS), { svgOrigin: "0 0", rotation: 0 });
      gsap.set(sel(p, ["faL", "faR"]), { rotation: -35 });
    },

    /* Gehen oder Laufen: Beine und Arme wechseln im Takt. half = halbe Schrittdauer in s. */
    cycle: function (tl, p, t0, t1, o) {
      o = o || {};
      var half = o.half || 0.34, amp = o.amp || 26, arm = o.arm || 28, knee = o.knee || 24;
      var ease = "sine.inOut";
      var k = 0;
      for (var t = t0; t < t1 - 1e-6; t += half, k++) {
        var s = k % 2 === 0 ? 1 : -1;
        var d = Math.min(half, t1 - t);
        tl.to("#" + p + "-thL", { rotation: s * amp, duration: d, ease: ease }, t)
          .to("#" + p + "-thR", { rotation: -s * amp, duration: d, ease: ease }, t)
          .to("#" + p + "-shL", { rotation: s < 0 ? knee : 0, duration: d, ease: ease }, t)
          .to("#" + p + "-shR", { rotation: s > 0 ? knee : 0, duration: d, ease: ease }, t)
          .to("#" + p + "-uaL", { rotation: -s * arm, duration: d, ease: ease }, t)
          .to("#" + p + "-uaR", { rotation: s * arm, duration: d, ease: ease }, t);
      }
    },

    /* Beine und Oberarme zurück in die Grundhaltung. */
    rest: function (tl, p, t, d) {
      d = d || 0.2;
      tl.to(sel(p, ["thL", "thR", "shL", "shR", "uaL", "uaR"]), { rotation: 0, duration: d, ease: "sine.out" }, t);
    }
  };
})();
