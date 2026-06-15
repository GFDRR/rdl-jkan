---
attributions:
- entity:
    affiliation: null
    email: null
    name: "CONRED (Coordinadora Nacional Para la Reducci\xF3n de Desastres de Guatemala)"
    url: https://data.humdata.org/dataset/tabla-de-desastres-geodinamicos-y-geofisicos-e-hidrometeorologicos-ocurridos-desde-1530-al-ano-2015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "G\xE1ndara & Asociados"
    url: https://data.humdata.org/dataset/tabla-de-desastres-geodinamicos-y-geofisicos-e-hidrometeorologicos-ocurridos-desde-1530-al-ano-2015
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNICEF
    url: https://data.humdata.org/dataset/tabla-de-desastres-geodinamicos-y-geofisicos-e-hidrometeorologicos-ocurridos-desde-1530-al-ano-2015
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/tabla-de-desastres-geodinamicos-y-geofisicos-e-hidrometeorologicos-ocurridos-desde-1530-al-ano-2015
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/tabla-de-desastres-geodinamicos-y-geofisicos-e-hidrometeorologicos-ocurridos-desde-1530-al-ano-2015
dataset_id: rdls_lss-gtm_ocharolac_desastresgeodinamicosgeof_20160502
description: "Los indicadores contienen los eventos naturales ocurridos desde 1530\
  \ a 2015 sobre erupciones, terremotos, sismos, hundimientos, grietas, derrumbes\
  \ y eventos sobre ventarrones, correntadas, desbordamientos, temporales ,inundaci\xF3\
  n, lluvias, sequ\xEDas, huracanes, heladas, tempestades. Toda la informaci\xF3n\
  \ esta desagregada a nivel municipal.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/tabla-de-desastres-geodinamicos-y-geofisicos-e-hidrometeorologicos-ocurridos-desde-1530-al-ano-2015]"
details: "* [INFORM Guatemala.](http://www.inform-index.org/Subnational/Guatemala)\
  \ * Componente: Eventos Naturales * Categor\xEDa: Natural * Dimensi\xF3n: Peligro\
  \ y Exposici\xF3n"
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Historical registry of natural disaster events in Guatemala compiled
    from 1530 to 2015 by CONRED and partners, disaggregated at municipal level. Data
    covers seven hazard types (volcanic, seismic, landslide, wind, flood, drought,
    and extreme temperature events) documented through administrative records and
    historical archives. The dataset represents observed/recorded disaster occurrences
    rather than hazard modeling or exposure inventories.
  sources:
  - id: source_1
    license: null
    name: "CONRED (Coordinadora Nacional Para la Reducci\xF3n de Desastres de Guatemala)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "G\xE1ndara & Asociados"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: UNICEF
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tabla-de-desastres-geodinamicos-y-geofisicos-e-hidrometeorologicos-ocurridos-desde-1530-al-ano-2015
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Volcanic eruption events recorded from 1530 to 2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: Earthquake and seismic events recorded from 1530 to 2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: Landslide and subsidence events recorded from 1530 to 2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: Strong wind and hurricane events recorded from 1530 to 2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: Flood, overflow, and heavy rainfall events recorded from 1530 to
      2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: Drought events recorded from 1530 to 2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_6
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: Extreme cold (frost) events recorded from 1530 to 2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
    id: loss_7
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
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
  description: "Tabla de indicadores de desastres geodin\xE1micos y geof\xEDsicos\
    \ ocurridos desde 1530 al a\xF1o 2015."
  download_url: https://data.humdata.org/dataset/398d3093-bf49-4625-b4ec-275052d2e64d/resource/cda784c2-c84f-4a70-9fdb-54b5297214fe/download/1.1.1.a-desastres-geodinamicos-y-geofisicos-ocurridos-desde-1530-al-ano-2015.xlsx
  format: null
  id: resource_cda784c2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "1.1.1.A Desastres Geodin\xE1micos y Geof\xEDsicos ocurridos desde 1530 al\
    \ a\xF1o 2015.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Tabla de indicadores de desastres hidrometeorol\xF3gicos ocurridos\
    \ desde 1530 al a\xF1o 2015."
  download_url: https://data.humdata.org/dataset/398d3093-bf49-4625-b4ec-275052d2e64d/resource/51d1d933-4932-4b26-95b8-9548734eb3e0/download/1.1.1.b-desastres-hidrometereorologicos-ocurridos-desde-1530-al-ano-2015.xlsx
  format: null
  id: resource_51d1d933
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "1.1.1.B Desastres Hidrometereorol\xF3gicos ocurridos desde 1530 al a\xF1\
    o 2015.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_ocharolac_desastresgeodinamicosgeof_20160502
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
title: "Guatemala Desastres Geodin\xE1micos, Geof\xEDsicos e Hidrometeorol\xF3gicos\
  \ ocurridos desde 1530 al a\xF1o 2015"
version: null
vulnerability: null
---
