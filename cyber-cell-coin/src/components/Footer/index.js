import React from 'react';
import {animateScroll as scroll} from 'react-scroll';
import { FaFacebook, FaInstagram, FaTwitter } from 'react-icons/fa';
import {FooterContainer, FooterWrap, FooterLinksContainer, FooterLinksWrapper, FooterLinkItems, FooterLinkTitle, 
        FooterLink, SocialMedia, SocialMediaWrap, SocialLogo, WebsiteRights, SocialIcons, SocialIconLink} from './FooterElements'


const Footer = () => {

    const toggleHome = () => {
        scroll.scrollToTop()
    };
    
    return (
        <FooterContainer>
            <FooterWrap>
                <FooterLinksContainer>
                    <FooterLinksWrapper>
                        <FooterLinkItems>
                                <FooterLinkTitle> About Us </FooterLinkTitle>
                                    <FooterLink to="/signin">About us</FooterLink>
                                    <FooterLink to="/signin">How it works</FooterLink>
                                    <FooterLink to="/signin">Term of Services</FooterLink>
                            </FooterLinkItems>
                            <FooterLinkItems>
                                <FooterLinkTitle> Social Media </FooterLinkTitle>
                                    <FooterLink to="/signin">Facebook</FooterLink>
                                    <FooterLink to="/signin">Twitter</FooterLink>
                                    <FooterLink to="/signin">Instagram</FooterLink>
                            </FooterLinkItems>
                    </FooterLinksWrapper>
                </FooterLinksContainer>
                <SocialMedia>
                    <SocialMediaWrap>
                        <SocialLogo to='/' onClick={toggleHome}> CyberCell Coin</SocialLogo>
                        <WebsiteRights> Copyright © {new Date().getFullYear()} CyberCell Coin</WebsiteRights>
                        <SocialIcons>
                            <SocialIconLink href='/' target="_blank" aria-label="Facebook">
                                <FaFacebook />
                            </SocialIconLink>
                            <SocialIconLink href='/' target="_blank" aria-label="Twitter">
                                <FaTwitter />
                            </SocialIconLink>
                            <SocialIconLink href='/' target="_blank" aria-label="Instagram">
                                <FaInstagram />
                            </SocialIconLink>
                        </SocialIcons>
                    </SocialMediaWrap>
                </SocialMedia>
            </FooterWrap>         
        </FooterContainer>
    );
};

export default Footer
