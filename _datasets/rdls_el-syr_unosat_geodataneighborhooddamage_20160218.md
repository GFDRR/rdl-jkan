---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-neighborhood-damage-percentages-aleppo-syria-february-18-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-neighborhood-damage-percentages-aleppo-syria-february-18-2016
dataset_id: rdls_el-syr_unosat_geodataneighborhooddamage_20160218
description: 'This map illustrates the percentages of buildings damaged in the city
  of Aleppo, Syrian Arab Republic, as determined by satellite imagery analysis. Using
  satellite imagery acquired 01 May 2015, 26 April 2015, 23 May 2014, 23 September
  2013, and 21 November 2010, UNITAR - UNOSAT identified a total of 12,065 damaged
  structures within the extent of this map. These damaged structures are compared
  with total numbers of buildings found in a pre-conflict satellite image collected
  in 2009 to determine the percentage of damaged buildings across the city. Based
  on this analysis, in 12 neighborhoods the number of damaged buildings is more than
  20%, and the neighborhood with the most damage is al Aqabeh, with 42,53% of buildings
  damaged. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-neighborhood-damage-percentages-aleppo-syria-february-18-2016]'
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
    description: Building stock inventory across Aleppo neighborhoods with pre-conflict
      baseline from 2009 satellite imagery
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery acquired
    between 2009 and 2015 to identify structural damage in Aleppo. Damaged structures
    identified through visual interpretation of satellite imagery changes were counted
    and compared against a pre-conflict 2009 baseline to calculate damage percentages
    by neighborhood. Results are provided as spatial polygons with damage percentage
    attributes.
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
- href: https://data.humdata.org/dataset/geodata-of-neighborhood-damage-percentages-aleppo-syria-february-18-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed through satellite imagery comparison
      across Aleppo neighborhoods
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
  description: Geodata of Neighborhood Damage Percentages, Aleppo, Syria (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130404SYR_DamageAssessment_OFDA_REACH_UPDATE3_shp.zip
  format: null
  id: resource_dcec3516
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130404SYR_DamageAssessment_OFDA_REACH_UPDATE3_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Neighborhood Damage Percentages, Aleppo, Syria (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_OFDA_REACH_DA_UPDATE3.gdb.zip
  format: null
  id: resource_8cefa8be
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130604SYR_OFDA_REACH_DA_UPDATE3.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_geodataneighborhooddamage_20160218
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-02-18'
temporal_resolution: null
title: Geodata of Neighborhood Damage Percentages, Aleppo, Syria
version: null
vulnerability: null
---
