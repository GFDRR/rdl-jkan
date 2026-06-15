---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-1-grand-anse-departement-haiti
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-1-grand-anse-departement-haiti
dataset_id: rdls_lss-hti_unosat_preliminarybaseddamageass_20161020
description: 'This report describes preliminary building damage analysis carried out
  by UNITAR-UNOSAT covering Area 1 (Jeremie and Roseaux Commune) and Area 2 (Abricot,
  Dame-Marie, Anse d''Hainaults and Les Irois Communes) for a total area of approximately
  650 Km2. Building damage analysis, including a rapid assessment of transportation
  network conditions and locations of spontaneous people gathering sites, was conducted
  by comparing the post-disaster satellite images (Pleiades acquired on 7/10/2016
  for AOI1 and 12/10/2016 for AOI2) with available pre-disaster images (WorldView-1
  on 01/05/2015, 09/05/2015 and 08/12/2014; Worldview-2 on 17 July 2016).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-1-grand-anse-departement-haiti]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared post-disaster Pleiades satellite imagery\
    \ (acquired 7-12 October 2016) with pre-disaster WorldView-1 baseline imagery\
    \ (May 2015) to identify and map building damage and transportation network conditions\
    \ across Grand Anse D\xE9partement. Damage classification was derived from visual\
    \ interpretation of spectral and spatial changes in satellite imagery, with results\
    \ delivered as vector geodatabase and shapefile formats covering approximately\
    \ 650 km\xB2 across four communes."
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
- href: https://data.humdata.org/dataset/preliminary-satellite-based-damage-assessment-report-update-1-grand-anse-departement-haiti
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from tropical cyclone Matthew derived
      from satellite image comparison
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
    description: Transportation network damage and condition assessment from tropical
      cyclone Matthew
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
  description: "Preliminary Satellite Based Damage Assessment Report - UPDATE 1: Grand\
    \ Anse D\xE9partement, Haiti (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_gdb.zip
  format: Geodatabase
  id: resource_df19b1af
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
  description: "Preliminary Satellite Based Damage Assessment Report - UPDATE 1: Grand\
    \ Anse D\xE9partement, Haiti (Shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_shp.zip
  format: null
  id: resource_30eb05cb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003THI_combined_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_unosat_preliminarybaseddamageass_20161020
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
  start: '2016-10-20'
temporal_resolution: null
title: "Preliminary Satellite Based Damage Assessment Report - UPDATE 1: Grand Anse\
  \ D\xE9partement, Haiti"
version: null
vulnerability: null
---
