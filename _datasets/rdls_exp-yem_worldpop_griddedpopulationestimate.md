---
attributions:
- entity:
    affiliation: null
    email: null
    name: Common Operational Dataset on Population Statistics (COD-PS)
    url: https://data.humdata.org/dataset/population-yemen-2019-2023-using-codps-v1
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/population-yemen-2019-2023-using-codps-v1
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/population-yemen-2019-2023-using-codps-v1
dataset_id: rdls_exp-yem_worldpop_griddedpopulationestimate
description: 'These data were produced by WorldPop at the University of Southampton
  and World Bank Group . These data include gridded estimates of population at approximately
  100m for 2019, 2023 and 2024 along with estimates of the number of people belonging
  to individual age-gender groups. These results were produced using subnational population
  estimates for Yemen provided in the Common Operational Dataset on Population Statistics
  (2019, 2023 COD-PS and 2024 COD-PS ) and Subnational Administrative Boundaries for
  Yemen provided by OCHA . For further details, please, read the Release Statement
  . Recommended citations WorldPop and World Bank Group. 2024 Gridded population estimates
  for Yemen using UN COD-PS estimates 2019, 2023 and 2024, version 1.0 . https://data.worldpop.org/repo/prj/WP_WB/YEM/v1/
  License These data may be distributed using a Creative Commons Attribution 4.0 International
  (CC BY 4.0) License, specified in legal code. Contact release@worldpop.org for more
  information. The authors followed rigorous procedures designed to ensure that the
  used data, the applied method and thus the results are appropriate and of reasonable
  quality. If users encounter apparent errors or misstatements, they should contact
  WorldPop at release@worldpop.org. WorldPop, University of Southampton, and their
  sponsors offer these data on a ''where is, as is'' basis; do not offer an express
  or implied warranty of any kind; do not guarantee the quality, applicability, accuracy,
  reliability or completeness of any data provided; and shall not be liable for incidental,
  consequential, or special damages arising out of the use of any data that they offer..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-yemen-2019-2023-using-codps-v1]'
details: '**Recommended citations** WorldPop and World Bank Group. 2024 *Gridded population
  estimates for Yemen using UN COD-PS estimates 2019 , 2023 and 2024, version 1.0*.
  https://data.worldpop.org/repo/prj/WP_WB/YEM/v1/'
exposure:
- asset_type:
    description: Gridded population estimates at ~100m resolution with age-gender
      disaggregation for Yemen
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
  description: Subnational population estimates from UN COD-PS (2019, 2023, 2024)
    were spatially disaggregated to ~100m gridded resolution using WorldPop methodology,
    producing gridded population counts with age-gender stratification for disaster
    risk exposure assessment in Yemen.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Common Operational Dataset on Population Statistics (COD-PS)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-yemen-2019-2023-using-codps-v1
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This zip file contains 14 rasters in geotiff format at a spatial resolution
    of 3 arc-seconds (approximately 100m at the equator) contains estimates of total
    population size per grid cell across Yemen for 2024, along with estimates of the
    number of people belonging to 15-49 years age-gender group and children under
    5. For unconstrained, NA values represent areas that were mapped as water and
    for constrained NA values represent areas that were mapped as unsettled. These
    data are stored as floating-point numbers rather than integers to avoid rounding
    errors in aggregated populations for larger areas. Note: Population figures for
    2024 from UN OCHA do not have two districts ''YE1319'' and ''YE1324''. Therefore,
    both districts were set to 0 in the outputs.'
  download_url: https://data.worldpop.org/repo/prj/WP_WB/YEM/v1/yem_2024_pack1.zip
  format: null
  id: resource_fee90631
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yem_2024_pack1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This zip file contains 112 rasters in geotiff format at a spatial
    resolution of 3 arc-seconds (approximately 100m at the equator) contains estimates
    of total population size per grid cell across Yemen, along with estimates of the
    number of people belonging to individual age-gender groups. [Boys (0-17), Men
    (18+), Girls (0-17), Women (18+), Total /Women-Girl, Total MEN/Boys, 0 - 4...
    75 - 79, 80+]. For unconstrained, NA values represent areas that were mapped as
    water and for constrained NA values represent areas that were mapped as unsettled.
    These data are stored as floating-point numbers rather than integers to avoid
    rounding errors in aggregated populations for larger areas. Note: Population figures
    for 2024 from UN OCHA do not have two districts ''YE1319'' and ''YE1324''. Therefore,
    both districts were set to 0 in the outputs.'
  download_url: https://data.worldpop.org/repo/prj/WP_WB/YEM/v1/yem_2024_pack2.zip
  format: null
  id: resource_aad77786
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yem_2024_pack2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 14 rasters in geotiff format at a spatial resolution
    of 3 arc-seconds (approximately 100m at the equator) contains estimates of total
    population size per grid cell across Yemen, along with estimates of the number
    of people belonging to 15-49 years age-gender group and children under 5. For
    unconstrained, NA values represent areas that were mapped as water and for constrained
    NA values represent areas that were mapped as unsettled. These data are stored
    as floating-point numbers rather than integers to avoid rounding errors in aggregated
    populations for larger areas.
  download_url: https://data.worldpop.org/repo/prj/WP_WB/YEM/v1/yem_2023_pack1.zip
  format: null
  id: resource_bb17b462
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yem_2023_pack1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 112 rasters in geotiff format at a spatial resolution
    of 3 arc-seconds (approximately 100m at the equator) contains estimates of total
    population size per grid cell across Yemen, along with estimates of the number
    of people belonging to individual age-gender groups. [Boys (0-17), Men (18+),
    Girls (0-17), Women (18+), Total /Women-Girl, Total MEN/Boys, 0 - 4... 75 - 79,
    80+]. For unconstrained, NA values represent areas that were mapped as water and
    for constrained NA values represent areas that were mapped as unsettled. These
    data are stored as floating-point numbers rather than integers to avoid rounding
    errors in aggregated populations for larger areas.
  download_url: https://data.worldpop.org/repo/prj/WP_WB/YEM/v1/yem_2023_pack2.zip
  format: null
  id: resource_0ebd77f3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yem_2023_pack2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 14 rasters in geotiff format at a spatial resolution
    of 3 arc-seconds (approximately 100m at the equator) contains estimates of total
    population size per grid cell across Yemen, along with estimates of the number
    of people belonging to 15-49 years age-gender group and children under 5. For
    unconstrained, NA values represent areas that were mapped as water and for constrained
    NA values represent areas that were mapped as unsettled. These data are stored
    as floating-point numbers rather than integers to avoid rounding errors in aggregated
    populations for larger areas.
  download_url: https://data.worldpop.org/repo/prj/WP_WB/YEM/v1/yem_2019_pack1.zip
  format: null
  id: resource_59068aa2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yem_2019_pack1.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 112 rasters in geotiff format at a spatial resolution
    of 3 arc-seconds (approximately 100m at the equator) contains estimates of total
    population size per grid cell across Yemen, along with estimates of the number
    of people belonging to individual age-gender groups. [Boys (0-17), Men (18+),
    Girls (0-17), Women (18+), Total /Women-Girl, Total MEN/Boys, 0 - 4... 75 - 79,
    80+]. For unconstrained, NA values represent areas that were mapped as water and
    for constrained NA values represent areas that were mapped as unsettled. These
    data are stored as floating-point numbers rather than integers to avoid rounding
    errors in aggregated populations for larger areas.
  download_url: https://data.worldpop.org/repo/prj/WP_WB/YEM/v1/yem_2019_pack2.zip
  format: null
  id: resource_133031f3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yem_2019_pack2.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used.
  download_url: https://data.worldpop.org/repo/prj/WP_WB/YEM/v1/release_statement.pdf
  format: null
  id: resource_c31daa21
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: release_statement.pdf
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-yem_worldpop_griddedpopulationestimate
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Gridded Population Estimates for Yemen using UN COD-PS Estimates 2019, 2023
  and 2024, version 1.0
version: null
vulnerability: null
---
