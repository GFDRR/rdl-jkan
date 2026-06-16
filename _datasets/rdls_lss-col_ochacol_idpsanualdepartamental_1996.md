---
attributions:
- entity:
    affiliation: null
    email: null
    name: "UARIV (Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a las V\xED\
      ctimas)"
    url: https://data.humdata.org/dataset/idps-anual-departamental
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/idps-anual-departamental
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/idps-anual-departamental
dataset_id: rdls_lss-col_ochacol_idpsanualdepartamental_1996
description: "De acuerdo con el Observatorio del Programa Presidencial de Derechos\
  \ Humanos y Derecho Internacional Humanitario, se entiende por desplazamiento un\
  \ evento en el cual una o varias personas se han visto forzadas a migrar dentro\
  \ del territorio nacional, abandonando su localidad de residencia o actividades\
  \ econ\xF3micas habituales, porque su vida, su integridad f\xEDsica, su seguridad\
  \ o libertad personales han sido vulneradas o se encuentran directamente amenazadas,\
  \ con ocasi\xF3n de cualquiera de las siguientes situaciones: conflicto armado interno,\
  \ disturbios y tensiones interiores, violencia generalizada, violaciones masivas\
  \ de los derechos humanos, infracciones al Derecho Internacional Humanitario u otras\
  \ circunstancias emanadas de las situaciones anteriores, que puedan alterar o alteren\
  \ dr\xE1sticamente el orden p\xFAblico.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/idps-anual-departamental]"
details: "Los datos est\xE1n actualizados hasta la fecha carga de los datos, sin embargo\
  \ estos pueden cambiar ya que las v\xEDctimas de desplazamiento tienen dos a\xF1\
  os desde la ocurrencia del hecho victimizante para declarar ante el Ministerio P\xFA\
  blico. A partir de esta declaraci\xF3n, la UARIV dispone de 60 d\xEDas h\xE1biles\
  \ para surtir el proceso de valoraci\xF3n y decidir la inclusi\xF3n o no en el Registro\
  \ \xDAnico de V\xEDctimas."
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Annual departmental IDP counts compiled from the UARIV registry, which
    documents forced displacement events within Colombia caused by armed conflict,
    internal disturbances, and generalized violence. Data aggregated by administrative
    department to track displacement trends over time.
  sources:
  - id: source_1
    license: null
    name: "UARIV (Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a las V\xED\
      ctimas)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/idps-anual-departamental
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Annual internally displaced persons (IDPs) by department due to armed
      conflict, violence, and internal disturbances
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - IDPs anual departamental (La periodicidad de actualizaci\xF3\
    n de los datos ser\xE1 mensualmente)"
  download_url: https://data.humdata.org/dataset/87d5eb5f-cbeb-4a2f-81a1-a002f12e5156/resource/1f56da93-6622-477f-9b55-b109def3f248/download/idps-anuales-departamentales-junio-23-de-2015.csv
  format: null
  id: resource_1f56da93
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDPs anuales departamentales Junio 23 de 2015.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_idpsanualdepartamental_1996
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-06-23'
  start: '1996-12-01'
temporal_resolution: null
title: Colombia - IDPs anual departamental
version: null
vulnerability: null
---
