---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook AI and Data for Good
    url: https://data.humdata.org/dataset/brazil-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/brazil-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/brazil-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/brazil-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-bra_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Brazil: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/brazil-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for Brazil disaggregated
      by age groups (children 0-5, youth 15-24, elderly 60+), sex (men, women), and
      reproductive status (women 15-49)
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across Brazil. Population estimates derived from publicly available
    census data and demographic statistics were overlaid on building locations and
    disaggregated by age group and sex to create high-resolution gridded population
    density maps at the settlement level.
  sources:
  - id: source_1
    license: null
    name: Facebook AI and Data for Good
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
- href: https://data.humdata.org/dataset/brazil-high-resolution-population-density-maps-demographic-estimates
  rel: source
loss:
  losses: []
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
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/54964df0-8d6a-4f65-ac10-bcf11499a9fe/download/bra_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_54964df0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/6d6f1ea3-c8d3-4dc0-b0ea-af9c92b14b48/download/bra_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_6d6f1ea3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/8d00d329-f873-4a20-baf2-01991d64ff57/download/bra_men_2019-06-01_csv.zip
  format: null
  id: resource_8d00d329
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/6ca29762-b872-4bf3-8f1b-1de9af7c5a05/download/bra_northeast_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_6ca29762
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northeast_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/9584758c-23d2-47c6-b430-c719e4c66d83/download/bra_northeast_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_9584758c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northeast_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/562e471e-ae6b-46f2-b2cc-2788621de7c7/download/bra_northeast_men_2019-06-01_geotiff.zip
  format: null
  id: resource_562e471e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northeast_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/8450bd09-2a1f-45df-a7e1-c1c5aba8a7f5/download/bra_northeast_women_2019-06-01_geotiff.zip
  format: null
  id: resource_8450bd09
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northeast_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/94332c06-f80a-47af-ae24-c2cb4c3083ab/download/bra_northeast_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_94332c06
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northeast_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/c1fe8710-448b-4c5a-80ac-0556bff0bb82/download/bra_northeast_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_c1fe8710
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northeast_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/fbf50179-f677-4a7e-a814-6fa990877a10/download/bra_northwest_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_fbf50179
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northwest_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/c5a2e025-7781-44f7-9772-a780d0100001/download/bra_northwest_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_c5a2e025
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northwest_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/84859064-baba-4093-9a32-96e5e50b6b0a/download/bra_northwest_men_2019-06-01_geotiff.zip
  format: null
  id: resource_84859064
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northwest_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/40f6585d-411e-4fdf-9b0b-da683e3e9b01/download/bra_northwest_women_2019-06-01_geotiff.zip
  format: null
  id: resource_40f6585d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northwest_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/855b63d6-af91-4774-806f-9cb44bea7337/download/bra_northwest_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_855b63d6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northwest_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/8d0764dd-55da-419a-aac4-839b6f91dbdb/download/bra_northwest_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_8d0764dd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_northwest_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/5fe010a1-0aa8-4249-b0fd-bade33124e3b/download/bra_southeast_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_5fe010a1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southeast_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/f2b48b1f-450c-433b-8505-bf9ad6a987f9/download/bra_southeast_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_f2b48b1f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southeast_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/ea9b60aa-f245-438a-bdfa-30e3ff4a6391/download/bra_southeast_women_2019-06-01_geotiff.zip
  format: null
  id: resource_ea9b60aa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southeast_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/c9158e93-90d0-44cc-897d-fc1a960a4471/download/bra_southeast_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_c9158e93
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southeast_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/dc0edb72-732f-4508-98a3-dd620534b4af/download/bra_southeast_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_dc0edb72
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southeast_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/a33e807b-850b-4b63-92ec-b04d51f2c5d0/download/bra_southwest_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_a33e807b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southwest_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/3b8622ff-5dac-405a-b51c-68b9a350de12/download/bra_southwest_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_3b8622ff
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southwest_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/e8b765c1-9683-4a91-921b-3dcc84871520/download/bra_southwest_men_2019-06-01_geotiff.zip
  format: null
  id: resource_e8b765c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southwest_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/8784c37c-836c-4c3d-ae43-a70d69b022bf/download/bra_southwest_women_2019-06-01_geotiff.zip
  format: null
  id: resource_8784c37c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southwest_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/a49fbeca-5aff-44dd-9fc0-eeb1fb5d8d1a/download/bra_southwest_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_a49fbeca
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southwest_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/879440dd-12cc-48d3-a159-d13bc76d5ec3/download/bra_southwest_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_879440dd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southwest_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/3a8e1355-abb3-4dd9-9b3a-9b983af42b0e/download/bra_women_2019-06-01_csv.zip
  format: null
  id: resource_3a8e1355
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/b6613904-021c-4d56-88a7-61ad34087103/download/bra_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_b6613904
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/0e4af4ff-e4e5-4686-a17c-c8b326d98d76/download/bra_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_0e4af4ff
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/17bedf4e-c521-4fe2-865a-1d7c1469b4a5/download/population_bra_northeast_2018-10-01.zip
  format: null
  id: resource_17bedf4e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_bra_northeast_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/566d54d2-ec13-4f13-b948-35a7c707e04a/download/population_bra_northwest_2018-10-01.zip
  format: null
  id: resource_566d54d2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_bra_northwest_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/fcb2b647-a6e4-4725-b24d-563e6a4eb46a/download/population_bra_southeast_2018-10-01.zip
  format: null
  id: resource_fcb2b647
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_bra_southeast_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/d794ddc1-049c-41dd-b363-d35a5d1e8563/download/population_bra_southwest_2018-10-01.zip
  format: null
  id: resource_d794ddc1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_bra_southwest_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/957218ee-c740-44c0-88e5-7faeef813a0c/download/population_bra_northeast_2018-10-01.csv.zip
  format: null
  id: resource_957218ee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_bra_northeast_2018-10-01.csv..zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/1e1f271b-1055-4365-b391-f6fdf3093fe2/download/population_bra_northwest_2018-10-01.csv.zip
  format: null
  id: resource_1e1f271b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_bra_northwest_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/eb17516f-3c84-4626-95e4-df1f342f3d82/download/population_bra_southeast_2018-10-01.csv.zip
  format: null
  id: resource_eb17516f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_bra_southeast_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/5cb55d1a-9f11-4004-82f3-0c27e878495a/download/population_bra_southwest_2018-10-01.csv.zip
  format: null
  id: resource_5cb55d1a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_bra_southwest_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brazil: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c17003d1-47f4-4ec5-8229-2f77aeb114be/resource/3bde50a0-c349-4e53-bc2f-50a1636b6bd0/download/bra_southeast_men_2019-06-01_geotiff.zip
  format: null
  id: resource_3bde50a0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BRA_southeast_men_2019-06-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bra_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - BRA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-11-07'
  start: '2019-06-10'
temporal_resolution: null
title: 'Brazil: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
