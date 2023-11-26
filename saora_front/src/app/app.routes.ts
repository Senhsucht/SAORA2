import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioComponent } from './inicio/inicio.component';
import { FormularioInicioSesionComponent } from './formulario-inicio-sesion/formulario-inicio-sesion.component';
import { FormularioRegistroSocioComponent } from './formulario-registro-socio/formulario-registro-socio.component';

export const routes: Routes = [
    { path: '', component: InicioComponent},
    { path: 'login', component: FormularioInicioSesionComponent},
    { path: 'registro', component: FormularioRegistroSocioComponent},
];

@NgModule({
    imports: [RouterModule.forRoot(routes)]
})
export class AppRoutingModule { }
