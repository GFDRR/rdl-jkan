---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Ministerio de Salud P\xFAblica y Asistencia Social de Guatemala - SIGSA"
    url: https://data.humdata.org/dataset/guatemala-incidencia-en-peso-para-talla-en-menores-de-5-anos-por-desastres-naturales-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/guatemala-incidencia-en-peso-para-talla-en-menores-de-5-anos-por-desastres-naturales-2015
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/guatemala-incidencia-en-peso-para-talla-en-menores-de-5-anos-por-desastres-naturales-2015
dataset_id: rdls_lss-gtm_ocharolac_desnutricionagudaenmenore_20160502
description: "Peso para talla en menores de 5 a\xF1os (desnutrici\xF3n aguda) se utiliza\
  \ para evaluar Incidencia de los desastres naturales recientes Mitch 1998, Stan\
  \ 2005, Agatha y volc\xE1n de Pacaya 2010 y E12 2012. Este es un indicador que eval\xFA\
  a la desnutrici\xF3n aguda por hambre.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/guatemala-incidencia-en-peso-para-talla-en-menores-de-5-anos-por-desastres-naturales-2015]"
details: "* [INFORM Guatemala.](http://www.inform-index.org/Subnational/Guatemala)\
  \ * Componente: Poblaci\xF3n Desprotegida * Sub Componente: Poblaci\xF3n Infantil\
  \ afectada por desastres naturales * Categor\xEDa: Otros grupos vulnerables * Dimensi\xF3\
  n: Vulnerabilidad"
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Health surveillance data from Guatemala's national health registry
    (SIGSA) documenting acute malnutrition indicators in children under 5 years, analyzed
    to evaluate the indirect health impacts of specific natural disaster events (Hurricane
    Mitch 1998, Stan 2005, Agatha and Pacaya volcano 2010, E12 2012) on nutritional
    status.
  sources:
  - id: source_1
    license: null
    name: "Ministerio de Salud P\xFAblica y Asistencia Social de Guatemala - SIGSA"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/guatemala-incidencia-en-peso-para-talla-en-menores-de-5-anos-por-desastres-naturales-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition (weight-for-height) in children under 5 years
      as indirect impact from natural disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition (weight-for-height) in children under 5 years
      as indirect impact from volcanic activity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
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
  description: "Impacto eventos naturales en la desnutrici\xF3n aguda (Peso para Talla)\
    \ en menores de 5 a\xF1os, a\xF1o 2015."
  download_url: https://data.humdata.org/dataset/1b2491ff-5dfc-4795-b814-b216e4fbf4da/resource/e65c1b1e-5b5a-4542-a140-d7850899c3ed/download/2.2.2.2.a-incidencia-en-peso-para-talla-en-menores-de-5-anos-por-desastres-naturales.xlsx
  format: null
  id: resource_e65c1b1e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "2.2.2.2.A Incidencia en peso para talla en menores de 5 a\xF1os por desastres\
    \ naturales.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_ocharolac_desnutricionagudaenmenore_20160502
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-05-02'
temporal_resolution: null
title: "Guatemala Desnutrici\xF3n Aguda en menores de 5 a\xF1os por desastres naturales\
  \ 2015"
version: null
vulnerability: null
---
