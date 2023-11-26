import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormularioRegistroSocioComponent } from './formulario-registro-socio.component';

describe('FormularioRegistroSocioComponent', () => {
  let component: FormularioRegistroSocioComponent;
  let fixture: ComponentFixture<FormularioRegistroSocioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FormularioRegistroSocioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FormularioRegistroSocioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
