---
attributions:
- entity:
    affiliation: null
    email: null
    name: Malawi Department of Disaster Management Affairs (DoDMA)
    url: https://data.humdata.org/dataset/malawi-affected-persons-locations-0
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/malawi-affected-persons-locations-0
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Shelter Cluster
    url: https://data.humdata.org/dataset/malawi-affected-persons-locations-0
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/malawi-affected-persons-locations-0
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/malawi-affected-persons-locations-0
dataset_id: rdls_lss-mwi_ocharosea_displacementtrackingmatri_20150306
description: 'DTM (Displacement Tracking Matrix) IDP Sites in the Southern Region
  of Malawi, including the number of IDP''s per site, as at 6 March 2015 (Google Earth
  kmz file).. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-affected-persons-locations-0]'
details: '**Languages:** EN'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDP site locations and population counts were collected through the
    Displacement Tracking Matrix (DTM) methodology, a standardized IOM approach for
    tracking internally displaced populations. Data was compiled collaboratively by
    DoDMA, IOM, and the Shelter Cluster for the Southern Region of Malawi as of 6
    March 2015, and delivered as georeferenced point data (KMZ format) representing
    displacement sites and associated IDP populations.
  sources:
  - id: source_1
    license: null
    name: Malawi Department of Disaster Management Affairs (DoDMA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Shelter Cluster
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/malawi-affected-persons-locations-0
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flooding events, tracked by site
      location and population count
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malawi - Displacement Tracking Matrix (Zipped kmz)
  download_url: https://data.humdata.org/dataset/c1fa0b3d-2926-4949-b1f0-e4edebbdf31a/resource/0c020b75-1186-43b3-8326-3ec2ffa8cc9f/download/04_dtm-idp-site-as-06th-march-2015.zip
  format: null
  id: resource_0c020b75
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 04_DTM IDP Site as 06th March 2015.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mwi_ocharosea_displacementtrackingmatri_20150306
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-03-06'
temporal_resolution: null
title: Malawi - Displacement Tracking Matrix
version: null
vulnerability: null
---
