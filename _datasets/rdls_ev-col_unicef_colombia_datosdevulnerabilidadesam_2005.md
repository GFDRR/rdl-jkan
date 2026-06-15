---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNGRD
    url: https://data.humdata.org/dataset/datos-de-vulnerabilidades-amenazas-y-capacidades
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: SISBEN
    url: https://data.humdata.org/dataset/datos-de-vulnerabilidades-amenazas-y-capacidades
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: DANE
    url: https://data.humdata.org/dataset/datos-de-vulnerabilidades-amenazas-y-capacidades
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/datos-de-vulnerabilidades-amenazas-y-capacidades
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNICEF
    url: https://data.humdata.org/dataset/datos-de-vulnerabilidades-amenazas-y-capacidades
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Colombia (inactive)
  url: https://data.humdata.org/dataset/datos-de-vulnerabilidades-amenazas-y-capacidades
creator:
  affiliation: null
  email: null
  name: UNICEF Colombia (inactive)
  url: https://data.humdata.org/dataset/datos-de-vulnerabilidades-amenazas-y-capacidades
dataset_id: rdls_ev-col_unicef_colombia_datosdevulnerabilidadesam_2005
description: "Colecci\xF3n de indicadores (directos y proxy) sobre vulnerabilidades,\
  \ amenazas y capacidades de respuesta a principales riesgos por desastres naturales\
  \ o emergencias complejas que afectan a ni\xF1as, ni\xF1os y adolescentes.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/datos-de-vulnerabilidades-amenazas-y-capacidades]"
details: "Algunos indicadores agrupados bajo amenazas son estimaciones hechas por\
  \ OCHA o UNICEF que no necesariamente coinciden con los posibles c\xE1lculos de\
  \ fuentes oficiales nacionales. Estos indicadores han sido sistematizados, recopilados\
  \ y agrupados con fines estrictamente acad\xE9micos. Los datos aqui presentados\
  \ no reflejan los c\xE1lculos oficiales de las fuentes ni los de UNICEF. Se recomienda\
  \ verificar todos los datos con las fuentes oficiales."
exposure:
- asset_type:
    description: Child and adolescent population exposed to natural disasters and
      complex emergencies
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: This dataset aggregates direct and proxy indicators from multiple Colombian
    government agencies (UNGRD, SISBEN, DANE) and humanitarian organizations (OCHA,
    UNICEF) to construct composite vulnerability, hazard threat, and response capacity
    indices specifically for children and adolescents. The indicators are integrated
    to assess susceptibility to natural disasters and complex emergencies at the national
    level.
  sources:
  - id: source_1
    license: null
    name: UNGRD
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: SISBEN
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: DANE
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: OCHA
    risk_data_type:
    - vulnerability
    type: dataset
    url: null
    used_in: vulnerability
  - id: source_5
    license: null
    name: UNICEF
    risk_data_type:
    - vulnerability
    type: dataset
    url: null
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/datos-de-vulnerabilidades-amenazas-y-capacidades
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Datos de vulnerabilidades, amenazas y capacidades (Excel)
  download_url: https://data.humdata.org/dataset/34526a9a-8487-4998-9326-ab568666b810/resource/454b6c1f-f446-44dc-8aa6-c035b73d4b4c/download/indicadores-vulenrabilidad-amenaza-capacidades.xlsx
  format: null
  id: resource_454b6c1f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Indicadores-vulenrabilidad-amenaza-capacidades.xlsx
risk_data_type:
- exposure
- vulnerability
schema: rdls-10
slug: rdls_ev-col_unicef_colombia_datosdevulnerabilidadesam_2005
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
  end: '2013-12-31'
  start: '2005-01-01'
temporal_resolution: null
title: Colombia - Datos de vulnerabilidades, amenazas y capacidades
version: null
vulnerability: null
---
