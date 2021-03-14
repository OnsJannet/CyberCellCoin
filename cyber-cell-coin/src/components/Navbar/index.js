import React from 'react'
import { FaBars } from 'react-icons/fa';
import{
    Nav, 
    NavbarContainer, 
    NavLogo, 
    MobileIcon, 
    NavMenu, 
    NavItem, 
    NavLinks,
    NavBtn,
    NavBtnLink}
from './NavbarElemnts';



const Navbar = () => {
    return (
        <>
            <Nav>
                <NavbarContainer>
                    <NavLogo to='/'>CyberCell</NavLogo>
                    <MobileIcon>
                        <FaBars />
                    </MobileIcon>
                    <NavMenu>
                        <NavItem>
                            <NavLinks to='Home'>Home</NavLinks>
                        </NavItem>
                        <NavItem>
                            <NavLinks to='OverView'>OverView</NavLinks>
                        </NavItem>
                        <NavItem>
                            <NavLinks to='Team'>Team</NavLinks>
                        </NavItem>
                        <NavItem>
                            <NavLinks to='Howitworks'>How it works</NavLinks>
                        </NavItem>
                        <NavItem>
                            <NavLinks to='signup'>Sign UP</NavLinks>
                        </NavItem>
                    </NavMenu>
                    <NavBtn>
                        <NavBtnLink to="/signin">Sign In</NavBtnLink>
                    </NavBtn>

                </NavbarContainer>
            </Nav>
        </>
    );
};

export default Navbar
