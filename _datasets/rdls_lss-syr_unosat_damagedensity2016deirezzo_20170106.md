---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-2016-of-deir-ez-zor-deir-ez-zor-governorate-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-2016-of-deir-ez-zor-deir-ez-zor-governorate-syria
dataset_id: rdls_lss-syr_unosat_damagedensity2016deirezzo_20170106
description: 'This map illustrates satellite-detected damage density in a portion
  of the city of Deir Ez Zor, Syrian Arab Republic. Using satellite imagery acquired
  25 May 2016, 10 May 2015, 13 May 2014, and 24 October 2013, UNITAR - UNOSAT identified
  a total of 4,595 affected structures within the city. Approximately 786 of these
  were destroyed, 1,386 severely damaged, and 2,423 moderately damaged. While much
  of the city was damaged by 10 May 2015, 1,344 structures were newly damaged and
  67 structures experienced an increase in damage between that date and 25 May 2016.
  This analysis does not include pre-war military bases and facilities. This analysis
  was done as part of the REACH initiative for the U.S. Office of Foreign Disaster
  Assistance. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-density-2016-of-deir-ez-zor-deir-ez-zor-governorate-syria]'
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
  description: UNOSAT analysts compared satellite imagery acquired on four dates (24
    October 2013, 13 May 2014, 10 May 2015, and 25 May 2016) over Deir Ez Zor city
    to identify structural damage through visual change detection. Buildings were
    classified into three damage categories (destroyed, severely damaged, moderately
    damaged) and temporal changes in damage status were tracked between consecutive
    image pairs to produce a damage density assessment.
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
- href: https://data.humdata.org/dataset/damage-density-2016-of-deir-ez-zor-deir-ez-zor-governorate-syria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Deir Ez Zor
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
  description: Syria - Damage density 2016 of Deir Ez Zor, Deir Ez Zor Governorate
    (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
  format: null
  id: resource_796bf86f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_unosat_damagedensity2016deirezzo_20170106
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
  start: '2017-01-06'
temporal_resolution: null
title: Syria - Damage density 2016 of Deir Ez Zor, Deir Ez Zor Governorate
version: null
vulnerability: null
---
