---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNGRD
    url: https://data.humdata.org/dataset/desastres-naturales
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/desastres-naturales
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/desastres-naturales
dataset_id: rdls_lss-col_ochacol_desastresnaturales_2008
description: "Los desastres naturales tenidos en cuenta en la base de datos son: accidente,\
  \ accidente a\xE9reo, accidente de transito, accidente mar\xEDtimo, accidente minero,\
  \ avalancha, colapso, contaminaci\xF3n, creciente s\xFAbita, deslizamiento, erosi\xF3\
  n, explosi\xF3n, granizada, incendio estructural, incendio forestal, incendio vehicular,\
  \ inundaci\xF3n, otros, sequ\xEDa, sismo, tormenta el\xE9ctrica y vendaval. Para\
  \ esta base de datos anual se tuvo en cuenta las personas afectadas en estos diversos\
  \ eventos.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/desastres-naturales]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Annual registry of natural disaster events in Colombia compiled by
    UNGRD, documenting affected populations across 22 hazard categories including
    floods, landslides, earthquakes, droughts, storms, and wildfires. Data aggregated
    from disaster reports and impact assessments to track humanitarian impacts by
    event type.
  sources:
  - id: source_1
    license: null
    name: UNGRD
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/desastres-naturales
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People affected by landslides
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by floods and flash floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by droughts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by earthquakes
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by strong winds and storms
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by structural and forest fires
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_6
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by hail and lightning storms
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_7
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
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
  description: Colombia - Desastres Naturales (Desastres naturales anual.csv)
  download_url: https://data.humdata.org/dataset/71632441-ebba-45e8-bda9-71718cef10cc/resource/cafc5331-e462-408f-affc-2e418f56712e/download/desastres-naturales-anual.csv
  format: null
  id: resource_cafc5331
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desastres naturales anual.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_desastresnaturales_2008
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
  end: '2015-01-01'
  start: '2008-01-01'
temporal_resolution: null
title: Colombia - Desastres Naturales
version: null
vulnerability: null
---
