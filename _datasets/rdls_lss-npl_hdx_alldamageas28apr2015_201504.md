---
attributions:
- entity:
    affiliation: null
    email: null
    name: US National Geospatial Agency IWG-R3
    url: https://data.humdata.org/dataset/nepal-all-damage-as-of-28-apr-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/nepal-all-damage-as-of-28-apr-2015
creator:
  affiliation: null
  email: null
  name: US National Geospatial Agency IWG-R3
  url: https://data.humdata.org/dataset/nepal-all-damage-as-of-28-apr-2015
dataset_id: rdls_lss-npl_hdx_alldamageas28apr2015_201504
description: 'Geodata of nepal earthquake damages as of 28 April 2015 shared publicly
  by NGA''s Open Data Application .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nepal-all-damage-as-of-28-apr-2015]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Damage assessment data collected by the US National Geospatial Agency
    through remote sensing and ground surveys following the 2015 Nepal earthquake,
    compiled into geodatasets with damage classifications and spatial attributes as
    of 27-28 April 2015.
  sources:
  - id: source_1
    license: null
    name: US National Geospatial Agency IWG-R3
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nepal-all-damage-as-of-28-apr-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the 2015 Nepal earthquake
      as of 28 April 2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Polygon of damage assessment of Nepal earthquake as of 27 Apr 2015,
    in zipped shapefiles (48 kb)
  download_url: https://data.humdata.org/dataset/3cf4fc91-1d7d-4ae3-a3f1-0e80278c2e30/resource/666588bd-4744-470b-9072-4d3e5e7d74b5/download/all-damage-nepal-april-27th-2015.zip
  format: null
  id: resource_666588bd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: All_Damage_Nepal_April_27th_2015.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Polygon of damage assessment Nepal earthquake by 28 Apr 2015, in zipped
    shapefiles (257 kb)
  download_url: https://data.humdata.org/dataset/3cf4fc91-1d7d-4ae3-a3f1-0e80278c2e30/resource/96fcde8c-ec79-4096-953e-1e5adc4a4731/download/all-damage-nepal-april-28th-2015.zip
  format: null
  id: resource_96fcde8c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: All_Damage_Nepal_April_28th_2015.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_hdx_alldamageas28apr2015_201504
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-04-28'
  start: '2015-04-27'
temporal_resolution: null
title: 'Nepal: all damage as of 28 Apr 2015'
version: null
vulnerability: null
---
