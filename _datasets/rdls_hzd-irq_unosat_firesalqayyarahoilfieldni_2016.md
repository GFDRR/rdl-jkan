---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-13-march-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-13-march-2017
dataset_id: rdls_hzd-irq_unosat_firesalqayyarahoilfieldni_2016
description: 'This map illustrates satellite-detected fires and smoke plumes at oil
  wells south of Mosul, and also east of Baiji, Iraq. The Mosul fires began with an
  initial fire at one or two wells on 8 May 2016, lasting less than one day, and intermittently
  burned in June. The current fire complex began on 3 July with daily fire detections
  occurring until about 12 July, when the fires greatly increased in number and continued
  to burn until gradual reductions in detected fires occurred starting in November
  2016. The fires east of Baiji have been active since early January 2016. The frequency
  of smoke plumes (in days) is symbolized in shades of red and yellow, and was calculated
  using daily MODIS satellite images collected between 18 July 2016 and 13 March 2017.
  Note that as the plume dissipates then areas of thinner smoke are not detected in
  this process. The inset on the top right corner shows the infrared data from a Landsat
  image collected on 25 February 2017, indicating the Mosul fires in white. The inset
  on the top left corner, from 5 March 2017, shows the same area in real color. Additionally,
  precipitation data from NASA''s IMERG algorithm was included to evaluate instances
  of rainfall intersecting the smoke plume. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-13-march-2017]'
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery over the Al
    Qayyarah oil field complex to detect active fires and smoke plumes, identifying
    fire initiation dates, spatial extent, and temporal evolution from January 2016
    through November 2016. Fire locations and smoke frequency were mapped as vector
    features with spatial coordinates.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/fires-at-the-al-qayyarah-oil-field-nineveh-governorate-between-18-july-2016-and-13-march-2017
  rel: source
loss: null
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
  description: Iraq - Fires at the Al Qayyarah oil field, Nineveh Governorate (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Al_Qayyarah_oil_fires.gdb.zip
  format: Geodatabase
  id: resource_955231ca
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Al_Qayyarah_oil_fires.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Fires at the Al Qayyarah oil field, Nineveh Governorate (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Al_Qayyarah_oil_fires.shp.zip
  format: null
  id: resource_699a9659
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Al_Qayyarah_oil_fires.shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-irq_unosat_firesalqayyarahoilfieldni_2016
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
  end: '2017-03-13'
  start: '2016-07-18'
temporal_resolution: null
title: Iraq - Fires at the Al Qayyarah oil field, Nineveh Governorate
version: null
vulnerability: null
---
