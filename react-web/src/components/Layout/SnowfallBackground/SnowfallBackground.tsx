import React, { useEffect, useRef } from "react";
import "./SnowfallBackground.css";

const SnowfallBackground = () => {
  const containerRef: React.MutableRefObject<HTMLDivElement | null> = useRef(null);

  useEffect(() => {
    const container = containerRef.current;

    const createSnowflake = () => {
      if (!container) return;
      
      const snowflake = document.createElement("div");
      snowflake.classList.add("snowflake");
      snowflake.innerHTML = "❄";
      
      snowflake.style.left = Math.random() * 100 + "vw";
      snowflake.style.animationDuration = Math.random() * 5 + 3 + "s";
      snowflake.style.fontSize = Math.random() * 10 + 10 + "px";

      container.appendChild(snowflake);

      setTimeout(() => {
        snowflake.remove();
      }, 8000);
    }

    let lastTime = 0;
    function animate(time: number) {
      if (time - lastTime > 200) { // Máximo 5 copos por segundo
        createSnowflake();
        lastTime = time;
      }
      requestAnimationFrame(animate);
    }

    requestAnimationFrame(animate);

    return () => {
      if (container) {
        container.innerHTML = ""; 
      }
    };
  }, []);

  return <div className="snow-container" ref={containerRef}></div>;
};

export default SnowfallBackground;
