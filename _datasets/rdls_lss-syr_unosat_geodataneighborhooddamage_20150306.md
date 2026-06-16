---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-neighborhood-damage-assessment-kobane-aleppo-governorate-syria-march-06-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-neighborhood-damage-assessment-kobane-aleppo-governorate-syria-march-06-2015
dataset_id: rdls_lss-syr_unosat_geodataneighborhooddamage_20150306
description: 'This map illustrates satellite-detected damage and destruction per neighborhood
  in the city of Kobane, Aleppo Governorate, Syria. Using satellite imagery acquired
  22 January 2015 compared with imagery from 6 September 2014, UNITAR / UNOSAT identified
  a total of 2,730 affected structures by 22 January 2015 within the neighborhoods.
  Approximately 961 of these were destroyed, 969 severely damaged, and 800 moderately
  damaged. A total of 246 impact craters were also identified within the city of Kobane.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-neighborhood-damage-assessment-kobane-aleppo-governorate-syria-march-06-2015]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 22 January 2015
    with baseline imagery from 6 September 2014 to detect and classify building damage
    in Kobane. Damage was categorized into destroyed, severely damaged, and moderately
    damaged structures, with impact craters also identified. Results are presented
    as neighborhood-level damage assessments in vector format.
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
- href: https://data.humdata.org/dataset/geodata-of-neighborhood-damage-assessment-kobane-aleppo-governorate-syria-march-06-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction in Kobane,
      Syria
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
  description: Geodata of Neighborhood Damage Assessment Kobane, Aleppo Governorate,
    Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Kobane_20150122_shp.zip
  format: null
  id: resource_471324a4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kobane_20150122_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Neighborhood Damage Assessment Kobane, Aleppo Governorate,
    Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Kobane_20150122_gdb.zip
  format: null
  id: resource_d772a15f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kobane_20150122_gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_unosat_geodataneighborhooddamage_20150306
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
  start: '2015-03-06'
temporal_resolution: null
title: Geodata of Neighborhood Damage Assessment Kobane, Aleppo Governorate, Syria
version: null
vulnerability: null
---
