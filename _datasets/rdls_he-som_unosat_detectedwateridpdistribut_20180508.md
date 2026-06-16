---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-2792
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-2792
dataset_id: rdls_he-som_unosat_detectedwateridpdistribut_20180508
description: 'This map illustrates satellite-detected flood water extent and IDP distribtuion
  within the town of Belet Weyne in Belet Weyne District,Hiiran Region, Somalia. The
  analysis was conducted analyzing GeoEye-1 & WorldView-3 images acquired on the 30
  April & 1 May 2018. As observed from the satellite image, the town of Belet Weyne
  is completely affected by the floods. Around 70% of the extension of the town is
  totally inundated, being the districts of Bulahabley, Bundaweyn, Dhagahjebis, Hilac,
  Hindab and Lamagalay Regional Military Based, Radar and Kutimbo completely submerged
  in water. The flood waters inside areas of partially flooded districts are receding.
  More than 110 IDP sites are located inside the town, and 50% of them are inside
  areas completly flooded. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-2792]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Internally displaced persons (IDPs) distribution within Belet Weyne
      town
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared GeoEye-1 and WorldView-3 satellite images
    acquired on 30 April and 1 May 2018 to detect changes in water extent across Belet
    Weyne town. The analysis identified inundated areas and mapped IDP camp locations
    through visual interpretation of satellite imagery, producing vector geometries
    of flood-affected zones and population displacement sites.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-idp-distribution-over-belet-weyne-town-2792
  rel: source
loss: null
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
  description: Somalia - Satellite detected water & IDP distribution over Belet Weyne
    Town (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20180501SOM/FL20180501SOM_SHP.zip
  format: null
  id: resource_dcd07785
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180501SOM_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-som_unosat_detectedwateridpdistribut_20180508
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-08'
temporal_resolution: null
title: Somalia - Satellite detected water & IDP distribution over Belet Weyne Town
version: null
vulnerability: null
---
