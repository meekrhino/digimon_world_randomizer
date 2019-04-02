// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import MainContainer from "./MainContainer";

namespace global {
	declare namespace JSX {
		interface ElementAttributesProperty extends Object { }
	}
}
//Render the main container into the html
ReactDOM.render( <MainContainer/>, document.getElementById( 'MainContainer' ) )
