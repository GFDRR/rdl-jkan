---
attributions:
- entity:
    affiliation: null
    email: null
    name: Dominica Red Cross Society
    url: https://data.humdata.org/dataset/dominica-red-cross-assessment-data-20150917
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: MapAction
  url: https://data.humdata.org/dataset/dominica-red-cross-assessment-data-20150917
creator:
  affiliation: null
  email: null
  name: MapAction
  url: https://data.humdata.org/dataset/dominica-red-cross-assessment-data-20150917
dataset_id: rdls_lss-dma_mapaction_dominicaredcrossassessmen_20150917
description: 'Shapefile containing numbers of affected people and households in Dominica.
  The data also shows number of damaged buildings (destroyed, major and minor) as
  collated by the Dominica Red Cross as of 17 September 2015.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/dominica-red-cross-assessment-data-20150917]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Dominica Red Cross conducted a sample survey-based damage assessment
    following a convective storm event, collecting point-based observations of affected
    households, people, and building damage severity (destroyed/major/minor). Data
    was compiled and georeferenced as a shapefile by MapAction for spatial analysis
    of disaster impacts.
  sources:
  - id: source_1
    license: null
    name: Dominica Red Cross Society
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/dominica-red-cross-assessment-data-20150917
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by convective storm event in Dominica
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage (destroyed, major, minor) from convective
      storm event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dominica Red Cross Assessment Data 20150917 (Shapefile)
  download_url: https://data.humdata.org/dataset/4b48d41a-ac0c-4e08-b912-f43356ce9cc3/resource/53eb310a-16e3-4f52-9a7b-a2c142adaadb/download/dma_situ_aff_pt_s0_dana_pp_assessmentdata_20150917.zip
  format: null
  id: resource_53eb310a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dma_situ_aff_pt_s0_dana_pp_assessmentdata_20150917.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-dma_mapaction_dominicaredcrossassessmen_20150917
spatial:
  bbox: null
  centroid: null
  countries:
  - DMA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-09-17'
temporal_resolution: null
title: Dominica Red Cross Assessment Data 20150917
version: null
vulnerability: null
---
