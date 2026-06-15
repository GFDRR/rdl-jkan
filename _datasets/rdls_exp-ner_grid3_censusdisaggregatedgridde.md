---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Research Group
    url: https://data.humdata.org/dataset/census-disaggregated-gridded-population-estimates-for-niger-2021-version-1-0
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Niger National Census 2021
    url: https://data.humdata.org/dataset/census-disaggregated-gridded-population-estimates-for-niger-2021-version-1-0
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/census-disaggregated-gridded-population-estimates-for-niger-2021-version-1-0
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/census-disaggregated-gridded-population-estimates-for-niger-2021-version-1-0
dataset_id: rdls_exp-ner_grid3_censusdisaggregatedgridde
description: 'These data were produced by the WorldPop Research Group at the University
  of Southampton. This work was part of the GRID3 project with funding from the Bill
  and Melinda Gates Foundation and the United Kingdom''s Foreign, Commonwealth & Development
  Office (INV 009579, formerly OPP 1182425). Project partners included the United
  Nations Population Fund, Center for International Earth Science Information Network
  in the Columbia Climate School at Columbia University, and the Flowminder Foundation.
  Thomas Abbott (WorldPop) led the input processing and the modelling work following
  the Random Forest (RF)-based dasymetric mapping approach developed by Stevens et
  al. (2015). Heather Chamberlain, Sarchil Qader, and Attila N Lazar advised on the
  modelling procedure. The Institut National de la Statistique du Niger (INS) released
  the census-based total population projection using the results of the 2012 census
  of population and digital Commune boundaries. Engagement with INS was lead by Mathias
  Kuepie ( UNFPA ). The work was verseen by Attila N. Lazar and Andy J Tatem. For
  further details, please, read NER_population_v1_0_README.pdf. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/census-disaggregated-gridded-population-estimates-for-niger-2021-version-1-0]'
details: null
exposure:
- asset_type:
    description: Gridded population estimates disaggregated by age and sex derived
      from 2021 census data
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
  description: Census population counts from Niger's 2021 national census were spatially
    disaggregated into gridded estimates by WorldPop using their standard dasymetric
    mapping methodology, incorporating ancillary geospatial data to distribute population
    across fine-resolution grid cells with age-sex stratification.
  sources:
  - id: source_1
    license: null
    name: WorldPop Research Group
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Niger National Census 2021
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/census-disaggregated-gridded-population-estimates-for-niger-2021-version-1-0
  rel: source
loss:
  losses: []
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
  description: This geotiff raster, at a spatial resolution of 3 arc-seconds (approximately
    100m at the equator), contains estimates of the total population size per grid
    cell across Niger. NA values represent areas that were mapped as unsettled based
    on gridded building patterns derived from building footprints (Dooley and Tatem,
    2020). These data are stored as floating-point numbers rather than integers to
    avoid rounding errors in aggregated population totals for larger areas.
  download_url: https://wopr.worldpop.org/download/511
  format: null
  id: resource_9896d5a0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NER_population_v1_0_gridded.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used, and known assumptions
    and limitations of the results.
  download_url: https://wopr.worldpop.org/download/513
  format: null
  id: resource_8f9c064d
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NER_population_v1_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains 40 GeoTIFF rasters representing estimated population
    counts for specific age and sex groups within grid cells of approximately 100m.
    We provide 36 rasters for the commonly reported age-sex groupings of sequential
    age classes for males and females separately. These are labelled with either an
    'm' (male) or an 'f' (female) followed by the number of the first year of the
    age class represented by the data. 'f0' and 'm0' are population counts of under
    1-year olds for females and males, respectively. 'f1' and 'm1' are population
    counts of 1 to 4 year olds for females and males, respectively. Over 4 years old,
    the age groups are in five year bins labelled with a '5', '10', etc. Eighty year
    olds and over are represented in the groups 'f80' and 'm80'. We provide four additional
    rasters that represent demographic groups often targeted by programmes and interventions.
    These are 'under1' (all females and males under the age of 1), 'under5' (all females
    and males under the age of 5), 'under15' (all emales and males under the age of
    15) and 'f15_49' (all females between the ages of 15 and 49, inclusive).These
    data were produced post-hoc by multiplying the total population counts provided
    in the NER_population_v1_0_gridded.tif raster and age and sex proportions derived
    from the microcensus data for each province. While this data represents population
    counts, values contain decimals, i.e. fractions of people. This is because both
    the input population data and age-sex proportions contain decimals. For this reason,
    it is advised to aggregate the rasters at a coarser scale. For example, if four
    grid cells next to each other have values of 0.25 this indicates that there is
    1 person of that age group somewhere in those four grid cells.
  download_url: https://wopr.worldpop.org/download/512
  format: null
  id: resource_5a33745b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NER_population_v1_0_agesex.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster contains 1s for each approximately 100m grid cell
    (0.0008333 decimal degrees) across the study area. Zero values indicate grid cells
    that did not contain buildings and were therefore assumed to be unpopulated. NAs
    show grid cells considered as outside the study area.
  download_url: https://wopr.worldpop.org/download/510
  format: null
  id: resource_0d35f2d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NER_population_v1_0_mastergrid.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ner_grid3_censusdisaggregatedgridde
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Census disaggregated gridded population estimates for Niger (2021), version
  1.0.
version: null
vulnerability: null
---
