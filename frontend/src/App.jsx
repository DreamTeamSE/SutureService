import StartSection from "./assets/components/Home/StartSection"
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';


const theme = createTheme({
  palette: {
    mode: 'light', // Change to 'dark' for dark mode
    primary: {
      main: '#3B00B9', // Customize primary color
    },
    secondary: {
      main: '#dc004e', // Customize secondary color
    },
    background: {
      default: '#F2F8FF', // Background color for the app
    },
  },
});

// HIkfremfer


function App() {

  return (
    <>
     <ThemeProvider theme={theme}>
      <CssBaseline />
      <StartSection/>
      </ThemeProvider>
    </>
  )
}

export default App
