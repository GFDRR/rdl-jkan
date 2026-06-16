---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/american-samoa-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/american-samoa-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/american-samoa-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/american-samoa-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-asm_metad4g_americansamoahighresoluti_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in American Samoa: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/american-samoa-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.'"
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for overall
      population and demographic subgroups (women, men, children 0-5, youth 15-24,
      elderly 60+, women of reproductive age 15-49)
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to commercially available satellite imagery to identify building
    footprints, then overlaying population estimates derived from census data and
    demographic statistics in partnership with Columbia University. The resulting
    gridded datasets provide spatial distribution of total population and demographic
    subgroups at fine resolution across American Samoa.
  sources:
  - id: source_1
    license: null
    name: Facebook/Meta AI and Data for Good
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Columbia University
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/american-samoa-high-resolution-population-density-maps-demographic-estimates
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
  url: https://dataforgood.fb.com/docs/methodology-high-resolution-population-density-maps-demographic-estimates/
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://dataforgood.fb.com/docs/high-resolution-population-density-maps-demographic-estimates-documentation/
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://dataforgood.fb.com/docs/census-information-for-high-resolution-population-density-maps/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/44975c8e-ed2c-48b1-9a18-705a614917c3/download/asm_general_2020_geotiff.zip
  format: null
  id: resource_44975c8e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/b9641fcf-94b9-49e7-98a3-ad288ad0b629/download/asm_general_2020_csv.zip
  format: null
  id: resource_b9641fcf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/f4d930c8-e6c4-4c05-bcd1-a3eef3a35948/download/asm_children_under_five_2020_csv.zip
  format: null
  id: resource_f4d930c8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/e9649131-17a1-4fe8-864c-6aaed32bcf4b/download/asm_children_under_five_2020_geotiff.zip
  format: null
  id: resource_e9649131
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/c9941950-e95b-441b-a9bf-d50ea81bacd8/download/asm_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_c9941950
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/c83f048e-56cb-4c45-a68f-6aeab6b06936/download/asm_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_c83f048e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/de35c9fc-1eb5-429d-a3d1-12953fa0852d/download/asm_men_2020_csv.zip
  format: null
  id: resource_de35c9fc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/28405efa-8757-4a62-9533-b8f1d79decf8/download/asm_men_2020_geotiff.zip
  format: null
  id: resource_28405efa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/50328641-f589-48b5-9f52-634a74d16702/download/asm_women_2020_csv.zip
  format: null
  id: resource_50328641
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/bff6cabe-0c24-4687-9d65-406e039a0462/download/asm_women_2020_geotiff.zip
  format: null
  id: resource_bff6cabe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/b515d23f-0311-4807-a7a5-df3d8588dd49/download/asm_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_b515d23f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/7ec816ed-3cc8-4851-8ce0-cdf9c365eeea/download/asm_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_7ec816ed
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/9661cd47-8145-46fc-916c-a11a79cb3795/download/asm_youth_15_24_2020_csv.zip
  format: null
  id: resource_9661cd47
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'American Samoa: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/ed473d89-6d00-4c3a-b29a-eae1a8d20085/download/asm_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_ed473d89
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/abc4f0c3-6ab3-449c-a497-8aa7cd14566b/resource/9d9ded79-a5f2-4ce8-9de5-184462b11353/download/asm_dg_metadata.json.zip
  format: null
  id: resource_9d9ded79
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asm_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-asm_metad4g_americansamoahighresoluti_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - ASM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-04-29'
  start: '2019-06-19'
temporal_resolution: null
title: 'American Samoa: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
