---
attributions:
- entity:
    affiliation: null
    email: null
    name: METEOR Project (Modelling Exposure Through Earth Observation Routines)
    url: https://data.humdata.org/dataset/gambia-level-1-exposure-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Global Earthquake Model Foundation
  url: https://data.humdata.org/dataset/gambia-level-1-exposure-data
creator:
  affiliation: null
  email: null
  name: Global Earthquake Model Foundation
  url: https://data.humdata.org/dataset/gambia-level-1-exposure-data
dataset_id: rdls_exp-gmb_gem_level1exposuredata_20200505
description: 'This data was developed as part of the Modelling Exposure Through Earth
  Observation Routines (METEOR) project and is a Level 1, or a global-quality exposure
  data set. Minimal country-specific data was collected. The data is intended for
  CAT modeling and loss estimation. Repurposing this data for any reason other than
  assessing risk is not recommended. The data presents the estimated number of buildings,
  building area, and rebuilding value at a 15-arcsecond grid resolution (approximately
  500 meters at the equator). This data set is in point shapefile format where the
  points represent the centroids of the 15-arcsecond grid. The results were created
  through a process of spreading the number of buildings to the 15-arcsecond level
  by a statistical assessment of moderate resolution EO data, which is described in
  more detail in the dasymetric mapping lineage processing step. The estimated building
  count at any given area is a result of statistical processes and should not be mistaken
  as a building count. The structural classes of buildings used for risk assessment
  are estimated given the building wall, floor, and roof material classes surveyed
  through 2002 Population and Housing Census - Volume 1. Analytical report. Additionally,
  the data is provided in Open Exposure Data (OED) import format, as a pair of CSV
  files. One CSV file contains the location details, and the other is an ''account''
  file that is filled with default information to satisfy OED format requirements.
  The OED input files are set to use ''All perils'' (i.e. ''AA1''). All required OED
  account-related fields are populated with ''1'' by default (such as PortNumber,
  AccNumber, PolNumber). If you find this data useful please provide feedback via
  our questionnaire; it should take only a few minutes: https://forms.gle/DQjhE89CRegNKB3X8
  Please see the METEOR project page for information about the METEOR Project: http://meteor-project.org/
  Please see the METEOR map portal for interactive maps: https://maps.meteor-project.org/
  For more information about the Open Exposure Data (OED) standard, please see https://github.com/OasisLMF/OpenDataStandards.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/gambia-level-1-exposure-data]'
details: null
exposure:
- asset_type:
    description: Estimated number of buildings at 15-arcsecond grid resolution
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
license: CC-BY-4.0
lineage:
  description: The METEOR project developed a global-quality Level 1 exposure dataset
    for Gambia using Earth observation routines to estimate building stock characteristics
    (count, area, rebuilding value) at 15-arcsecond grid resolution (~500m). The data
    was processed into point shapefile format with grid-cell centroids and is intended
    for catastrophe modeling and disaster risk assessment.
  sources:
  - id: source_1
    license: null
    name: METEOR Project (Modelling Exposure Through Earth Observation Routines)
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gambia-level-1-exposure-data
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://meteor-project.org/documents/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: OED format (csv) Level 1 exposure data for Gambia produced by ImageCat
    and the METEOR project consortium.
  download_url: https://data.humdata.org/dataset/a3773c04-e167-4436-a822-3ced842ef6eb/resource/72357fe7-de21-4bf5-b240-d4a556ac89f5/download/gmb_oed_exposure_20200811_hdx.zip
  format: null
  id: resource_72357fe7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GMB_oed_exposure_20200811_hdx.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gmb_gem_level1exposuredata_20200505
spatial:
  bbox: null
  centroid: null
  countries:
  - GMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-05-05'
temporal_resolution: null
title: 'Gambia: Level 1 Exposure Data'
version: null
vulnerability: null
---
