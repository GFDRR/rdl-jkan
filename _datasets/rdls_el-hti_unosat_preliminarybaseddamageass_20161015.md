---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-grand-anse-departement-haiti
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-grand-anse-departement-haiti
dataset_id: rdls_el-hti_unosat_preliminarybaseddamageass_20161015
description: "This report highlights the preliminary building damage analysis including\
  \ a rapid assessment of transportation network conditions and locations of spontaneous\
  \ people gathering sites covering J\xE9r\xE9mie Commune and surrounding areas.The\
  \ analysis was conducted by comparing the post-disaster satellite images (Pleiades\
  \ acquired on 7/10/2016) with available pre-disaster images (WorldView-1 on 01/05/2015\
  \ and 08/12/2014).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-grand-anse-departement-haiti]"
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
    description: "Building stock assessed for damage in J\xE9r\xE9mie Commune and\
      \ surrounding areas"
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Transportation network conditions assessed post-disaster
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: "Satellite-based damage assessment conducted by UNOSAT analysts comparing\
    \ post-disaster Pleiades imagery acquired 7 October 2016 with pre-disaster WorldView-1\
    \ imagery from May and August 2014. Visual interpretation identified notable changes\
    \ in building structures and transportation networks in J\xE9r\xE9mie Commune,\
    \ Haiti following a tropical cyclone event, with results delivered as vector geodatabase\
    \ and shapefile formats."
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-grand-anse-departement-haiti
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone assessed via satellite
      imagery comparison
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct transportation network damage from tropical cyclone
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Preliminary Satellite Based Damage Assessment Report: Grand Anse D\xE9\
    partement, Haiti (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_gdb.zip
  format: Geodatabase
  id: resource_f95700e9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003THI_combined_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Preliminary Satellite Based Damage Assessment Report: Grand Anse D\xE9\
    partement, Haiti (Shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_shp.zip
  format: null
  id: resource_463c6f04
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003THI_combined_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-hti_unosat_preliminarybaseddamageass_20161015
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-15'
temporal_resolution: null
title: "Preliminary Satellite Based Damage Assessment Report: Grand Anse D\xE9partement,\
  \ Haiti"
version: null
vulnerability: null
---
