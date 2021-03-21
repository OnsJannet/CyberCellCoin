/*import React, {useState} from 'react'*/
import { FormButton, FormContent, FormH1, FormInput, FormLabel, FromWrap, Container, Icon, Form, Text } from './RegisterElements'
import Axios from 'axios'

const Register = () => {
    /*const [usernameReg, setUsernameReg] = useState('')
    const [PasswordReg, setPasswordReg] = useState('')
    const [FullNameReg, setFullNameReg] = useState('')
    const [EmailReg, setEmailReg] = useState('') */

    /*onChange={(e)=> {setFullNameReg.target.value}}*/
    /*onChange={(e)=> {setUsernameReg.target.value}}
    onChange={(e)=> {setPasswordReg.target.value}}*/

    return (
        <div>
            <Container>
                <FromWrap>
                    <Icon to="/">CyberCell Coin</Icon>
                    <FormContent>
                        <Form action="#">
                            <FormH1>Register New Account</FormH1>
                            <FormLabel htmlFor='for' required>Full Name</FormLabel>
                            <FormInput type='text' required  /> 
                            <FormLabel htmlFor='for' required>Username</FormLabel>
                            <FormInput type='text' required />
                            <FormLabel htmlFor='for' required>Email</FormLabel>
                            <FormInput type='email' required />
                            <FormLabel htmlFor='for'>Password</FormLabel>
                            <FormInput type='password' required />
                            <FormLabel htmlFor='for'>Confirm Password</FormLabel>
                            <FormInput type='password' required />
                            <FormButton type='submit'>Register</FormButton>
                            <Text>Forgot password</Text>
                        </Form>
                    </FormContent>
                </FromWrap>
            </Container>
        </div>
    )
}

export default Register
