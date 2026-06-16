---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sinjar-area-nineveh-province-iraq-december-02-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sinjar-area-nineveh-province-iraq-december-02-2015
dataset_id: rdls_lss-irq_unosat_geodatadamageassessmentsi_20151202
description: 'This map illustrates satellite-detected damage and destruction in the
  Sinjar area of Nineveh Province, Iraq. Using satellite imagery acquired 18 and 28
  November 2015, 30 December 2014, and 07 August 2014, UNITAR - UNOSAT identified
  a total of 1,780 potentially affected structures. Approximately 544 of these were
  destroyed, 473 severely damaged, 457 moderately damaged, and 306 possibly damaged.
  Note that due to less-than-ideal imagery characteristics the error margin for this
  analysis is likely higher than usual, and due to terrain distortion the spatial
  accuracy is +/- 15 meters. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sinjar-area-nineveh-province-iraq-december-02-2015]'
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
  description: "UNOSAT analysts compared satellite imagery acquired on multiple dates\
    \ (07 August 2014, 30 December 2014, 18 and 28 November 2015) over the Sinjar\
    \ area to identify structural damage through visual change detection. Building\
    \ damage was classified into four categories (destroyed, severely damaged, moderately\
    \ damaged, possibly damaged) based on satellite-detected changes, with spatial\
    \ accuracy of \xC2\xB115 meters and acknowledged higher error margins due to imagery\
    \ quality and terrain distortion."
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sinjar-area-nineveh-province-iraq-december-02-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Sinjar area
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
  description: Geodata of Damage Assessment of Sinjar Area, Nineveh Province, Iraq
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Sinjar_shp.zip
  format: null
  id: resource_19bd1b04
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Sinjar_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Sinjar Area, Nineveh Province, Iraq
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Sinjar.gdb.zip
  format: null
  id: resource_4246a1d8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Sinjar.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-irq_unosat_geodatadamageassessmentsi_20151202
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-12-02'
temporal_resolution: null
title: Geodata of Damage Assessment of Sinjar Area, Nineveh Province, Iraq
version: null
vulnerability: null
---
