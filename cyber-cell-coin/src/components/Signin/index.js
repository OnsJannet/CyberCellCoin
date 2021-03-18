import React from 'react'
import { FormButton, FormContent, FormH1, FormInput, FormLabel, FromWrap, Container, Icon, Form, Text } from './SigninElements'



const SignIn = () => {
    return (
        <div>
            <Container>
                <FromWrap>
                    <Icon to="/">CyberCell Coin</Icon>
                    <FormContent>
                        <Form action="#">
                            <FormH1>Sign in to your account</FormH1>
                            <FormLabel htmlFor='for' required>Email</FormLabel>
                            <FormInput type='email' required />
                            <FormLabel htmlFor='for'>Password</FormLabel>
                            <FormInput type='password' required />
                            <FormButton type='submit'>Continue</FormButton>
                            <Text>Forgot password</Text>
                            <Text>Don't Have An Account? Register Now </Text>
                            <Text> Home Page</Text>
                        </Form>
                    </FormContent>
                </FromWrap>
            </Container>
        </div>
    )
}

export default SignIn
