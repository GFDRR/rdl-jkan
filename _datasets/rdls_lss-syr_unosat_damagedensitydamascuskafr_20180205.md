---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-of-damascus-kafr-batna-and-irbin-subdistricts-damascus-governorate-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-of-damascus-kafr-batna-and-irbin-subdistricts-damascus-governorate-syria
dataset_id: rdls_lss-syr_unosat_damagedensitydamascuskafr_20180205
description: 'This map illustrates satellite-detected damage density in the subdistricts
  of Kafr Batna and Irbin and in the eastern part of Damascus city, Syrian Arab Republic.
  Using satellite imagery acquired 3 December 2017 and 2 April 2016, UNITAR - UNOSAT
  identified a total of 12,541 affected structures. Approximately 3,853 of these were
  destroyed, 5,141 severely damaged, and 3,547 moderately damaged. Comparison with
  the previous UNOSAT analysis using imagery from 2 April 2016 shows an overall increase
  of 6% in the number of damaged buildings since 2016. The areas with a higher increase
  in the percentage of damage are Ein Tarma (14% increase), Hammura (15% increase)
  and Kafr Batna (17 % increase). Moreover, approximately 7% of the buildings damaged
  as of April 2016 have been targeted again and suffered additional damage. The majority
  of these buildings are located in Ein Tarma, Jobar and Al Maamouniye. This is a
  preliminary analysis and has not yet been validated in the field. Please send ground
  feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-density-of-damascus-kafr-batna-and-irbin-subdistricts-damascus-governorate-syria]'
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 2 April 2016
    and 3 December 2017 over Damascus, Kafr Batna, and Irbin subdistricts to detect
    and classify building damage through visual interpretation. Damage was categorized
    into three classes (destroyed, severely damaged, moderately damaged) and quantified
    as structure counts per subdistrict, with temporal comparison showing 6% increase
    in damaged buildings over the 20-month period.
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
- href: https://data.humdata.org/dataset/damage-density-of-damascus-kafr-batna-and-irbin-subdistricts-damascus-governorate-syria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Damascus subdistricts
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
  description: Damage density of Damascus, Kafr Batna and Irbin subdistricts, Damascus
    Governorate, Syria (zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_Damascus_20171203_shp.zip
  format: null
  id: resource_811e7098
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Damascus_20171203_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_unosat_damagedensitydamascuskafr_20180205
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
  start: '2018-02-05'
temporal_resolution: null
title: Damage density of Damascus, Kafr Batna and Irbin subdistricts, Damascus Governorate,
  Syria
version: null
vulnerability: null
---
