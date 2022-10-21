import FullWidthLayout from 'hocs/Layouts/FullWidthLayout';
import React, { Component }  from 'react';
import { connect } from "react-redux";

function Home({
}){

    return(
        <FullWidthLayout>
           Home
        </FullWidthLayout>
    )
}

const mapStateToProps = state =>({
})

export default connect(mapStateToProps,{
})(Home)