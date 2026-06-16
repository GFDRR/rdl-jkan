---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tadmur-and-al-amiriyah-homs-governorate-syria-april-07-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tadmur-and-al-amiriyah-homs-governorate-syria-april-07-2016
dataset_id: rdls_lss-syr_unosat_geodatadamageassessmentta_20160407
description: 'This map illustrates the location of damaged structures in the cities
  of Tadmur and Al-Amiriyah in the Syrian Arab Republic. Using satellite imagery acquired
  30 March 2016, 18 October 2015, 27 August 2015, and 26 June 2015, UNITAR-UNOSAT
  identified a total of 611 damaged structures. Of these, 29 were destroyed, 103 severely
  damaged, and 479 moderately damaged. Additionally, a total of 66 craters were identified
  in the same area, an indicator of the level of fighting in these cities. Note that
  due to the nature of the combat and imagery quality it is likely that some minor
  and moderate damage has not been detected. UNITAR-UNOSAT will update this analysis
  as new imagery becomes available. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tadmur-and-al-amiriyah-homs-governorate-syria-april-07-2016]'
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
  description: UNOSAT analysts reviewed and compared satellite imagery acquired on
    four dates (26 June 2015, 27 August 2015, 18 October 2015, and 30 March 2016)
    to detect structural changes and damage in Tadmur and Al-Amiriyah. Damaged structures
    were classified into three severity categories (destroyed, severely damaged, moderately
    damaged) and spatially mapped as point features with damage classification attributes.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tadmur-and-al-amiriyah-homs-governorate-syria-april-07-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Tadmur and Al-Amiriyah
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
  description: Geodata of Damage Assessment of Tadmur and Al-Amiriyah, Homs Governorate,
    Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Palmyra_Tadmur_20160330_shp.zip
  format: null
  id: resource_d5c845be
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Palmyra_Tadmur_20160330_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Tadmur and Al-Amiriyah, Homs Governorate,
    Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Palmyra_Tadmur_20160330.gdb.zip
  format: null
  id: resource_c2347eeb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Palmyra_Tadmur_20160330.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_unosat_geodatadamageassessmentta_20160407
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
  start: '2016-04-07'
temporal_resolution: null
title: Geodata of Damage Assessment of Tadmur and Al-Amiriyah, Homs Governorate, Syria
version: null
vulnerability: null
---
