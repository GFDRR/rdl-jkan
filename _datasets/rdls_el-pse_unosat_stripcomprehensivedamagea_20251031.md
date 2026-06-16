---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-11-october-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-11-october-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-11-october-2025
dataset_id: rdls_el-pse_unosat_stripcomprehensivedamagea_20251031
description: 'UNOSAT code: CE20231007PSE This map illustrates a satellite imagery
  based comprehensive assessment of damage and destruction to structures within the
  area of interest in the Gaza Strip, Occupied Palestinian Territory. The analysis
  is based on images collected on 11 October 2025 when compared to images collected
  on 01 May 2023, 10 May 2023, 18 September 2023, 15 October 2023, 07 November 2023,
  26 November 2023, 06-07 January 2024, 29 February 2024, 31 March-01 April 2024,
  03 May 2024, 06 July 2024, 03-06 September 2024, 01 December 2024, 25 February 2025,
  04 April 2025, and 08 July 2025. According to satellite imagery analysis, as of
  11 October 2025, approximately 81% of all structures in the Gaza Strip are damaged.
  Among the damaged structures, UNOSAT identified 123,464 destroyed structures, 17,116
  severely damaged structures, 33,857 moderately damaged structures, and 23,836 possibly
  damaged structures for a total of 198,273 affected structures. Compared to the 8
  July 2025 assessment, this corresponds to a 4% increase in total affected structures,
  and an 18% increase in destroyed structures, indicating worsening damage. An estimated
  320,622 housing units have been damaged, 12% more than on 08 July 2025. The governorates
  of Gaza and North Gaza experienced the largest increases in damage compared to July
  2025, with approximately 4,243 newly affected structures in Gaza and 1,442 in North
  Gaza. According to the Population Movement Monitoring - 3rd Monthly Update from
  September 1-30, 379,851 people were displaced in September, with the majority of
  them being within the Gaza Governorate. In October, over 0.5 million people were
  displaced from the Gaza Governorate to the southern Governorates (until October
  10). This is a preliminary analysis and has not yet been validated in the field..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-11-october-2025]'
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
    description: Building structures assessed for damage status through satellite
      imagery comparison
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts conducted multi-temporal satellite imagery analysis
    comparing baseline images (May-November 2023) with post-event imagery (January
    2024-October 2025) to identify and classify building damage through visual interpretation
    of structural changes. Damage classifications were derived from observable changes
    in building footprints and structural integrity visible in high-resolution satellite
    imagery.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-11-october-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Gaza Strip
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
  description: Palestine - UNOSAT Gaza Strip Comprehensive Damage Assessment - 11
    October 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4213/OCHA-CBPF-OPT-031_UNOSAT_Gaza_Strip_CDA_11October2025_GDB.zip
  format: Geodatabase
  id: resource_32b28a8d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA-CBPF-OPT-031_UNOSAT_Gaza_Strip_CDA_11October2025_GDB.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_stripcomprehensivedamagea_20251031
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-10-31'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Strip Comprehensive Damage Assessment - 11 October
  2025
version: null
vulnerability: null
---
