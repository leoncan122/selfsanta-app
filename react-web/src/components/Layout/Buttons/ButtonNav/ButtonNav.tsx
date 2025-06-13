import React from 'react';
import './ButtonNav.css';
import { RightIcon } from '../../Header/RightIcon';
import { useLocation } from 'react-router-dom';

interface ButtonNavProps {
    label: string;
    icon: string;
    name: string;
    handleNavClick: (navItem: string) => void;
    totalNumeberOfNotifications: number;
}

const ButtonNav: React.FC<ButtonNavProps> = ({ handleNavClick, icon, name, totalNumeberOfNotifications }) => {
    
  const { pathname } = useLocation();
  const currentPath = pathname.split("/")[1] || "home";
  
  return (
        <li
              className={`button-list ${currentPath === name ? "active" : ""}`}
              onClick={() => handleNavClick(name)}
            >
              {name === "messages" ? (
                <RightIcon numberOfNotifications={totalNumeberOfNotifications}>
                  {icon}
                </RightIcon>
              ) : (
                icon
              )}
            </li>
    );
};

export default ButtonNav;